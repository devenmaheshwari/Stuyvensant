# CircleTable — Christopher Liu, Yusuf Elsharawy, Deven Maheshwari, Naomi Naranjo
# SoftDev
# P00: CircleStories

"""Routes

Handles all of the Flask app routes for CircleStories.
"""

from flask import render_template, redirect, request, url_for, session

from app import app
from app.auth import authenticate_user, create_user, get_user_id, get_username
from app.storydb import StoryDB

DB_FILE = "circlestories.db"

STORY_DB = StoryDB(DB_FILE)


def get_stories_info(story_ids):
    """Takes a list of story id's and returns a list of tuples of:
    (story_id, creator_username, story_title). This is useful
    for Jinja to list out stories."""
    result = []
    for story_id in story_ids:
        story_obj = STORY_DB.get_story(story_id)
        result.append((story_id, get_username(story_obj.creator_id), story_obj.title))
    return result


@app.route("/")
@app.route("/index")
def index():
    """CircleStories homepage."""
    if "username" in session:
        user_id = get_user_id(session["username"])

        contributed_stories = get_stories_info(
            STORY_DB.get_contributed_stories(user_id)
        )

        not_contributed_stories = get_stories_info(
            STORY_DB.get_not_contributed_stories(user_id)
        )

        return render_template(
            "homepage.html",
            username=session["username"],
            contributed_stories=contributed_stories,
            not_contributed_stories=not_contributed_stories,
        )

    return render_template("guest.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Displays login form and handles form response."""
    if "username" in session:
        return redirect(url_for("index"))

    # GET request: display the form
    if request.method == "GET":
        return render_template("login.html")

    # POST request: handle the form response and redirect
    username = request.form.get("username", default="")
    password = request.form.get("password", default="")

    if authenticate_user(username, password):
        session["username"] = username
        return redirect(url_for("index"))

    return render_template("login.html", error="Username or password incorrect")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Displays registration form and handles form response."""

    if "username" in session:
        return redirect(url_for("index"))

    # GET request: display the form
    if request.method == "GET":
        return render_template("register.html")

    # POST request: handle the form response and redirect
    username = request.form.get("username", default="")
    password = request.form.get("password", default="")
    password_check = request.form.get("password_check", default="")

    errors = create_user(username, password, password_check)
    if errors:
        return render_template("register.html", errors=errors)

    # Maybe put a flash message here to confirm everything works
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """Logs out the current user."""

    if "username" in session:
        del session["username"]
    return redirect(url_for("index"))


@app.route("/new_story", methods=["GET", "POST"])
def new_story():
    """Allows user to create to a new story."""

    if "username" not in session:
        return redirect(url_for("index"))

    # GET request: display the form
    if request.method == "GET":
        return render_template("new_story.html")

    # POST request: handle the form response and redirect
    created_story_title = request.form.get("title", default="")
    created_story_content = request.form.get("text", default="")
    created_story_image = request.form.get("image", default="")
    user_id = get_user_id(session["username"])

    story_id = STORY_DB.add_story(user_id, created_story_title)
    STORY_DB.get_story(story_id).add_block(
        user_id, created_story_content, created_story_image
    )

    return redirect(url_for("story", story_id=story_id))


@app.route("/story/<story_id>", methods=["GET", "POST"])
def story(story_id):
    """Given a story_id, displays the full story if the user has already
    contributed to it or provides an append form to add to the existing story."""

    if "username" not in session:
        return redirect(url_for("index"))
    user_id = get_user_id(session["username"])

    # Make sure the story exists
    story_obj = STORY_DB.get_story(story_id)
    if not story_obj:
        return render_template(
            "error.html",
            error_title="Story Not Found",
            error_msg="Sorry! This story was deleted or does not exist.",
        )

    # View entire story if user has contributed
    if STORY_DB.is_contributor(user_id, story_id):
        contributors = list(map(get_username, story_obj.get_contributors()))
        return render_template(
            "view_story.html",
            story_title=story_obj.title,
            story_blocks=zip(contributors, story_obj.get_blocks()),
        )

    # If user has not contributed, show append form
    if request.method == "GET":
        last_block = story_obj.last_block()
        return render_template(
            "append_story.html",
            story_id=story_id,
            story_title=story_obj.title,
            last_block=last_block,
        )

    # Handle story append response
    new_block_text = request.form.get("text", default="")
    new_block_img = request.form.get("image", default="")
    story_obj.add_block(user_id, new_block_text, new_block_img)
    return redirect(url_for("story", story_id=story_id))
