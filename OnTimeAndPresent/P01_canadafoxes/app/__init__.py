# Canada Foxes - Deven Maheshwari, Emma Buller, Lucas Lee, Naomi Naranjo
# SoftDev
# P01 - ArRESTed Development
# 2022-01-04

from os import urandom
from flask import Flask

app = Flask(__name__)

from app import routes
from app import db

# Secret key 32 bytes
app.secret_key = urandom(32)

# Database setup
# db.setup()

app.debug = True
app.run()
