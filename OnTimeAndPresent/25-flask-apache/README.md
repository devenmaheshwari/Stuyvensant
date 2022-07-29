# how-to :: Deploy Flask on Apache

## Overview
Allows us to host websites and other apps on easily accessible virtual servers.

### Estimated Time Cost: 1.5 hours

### Prerequisites:
0. Have a droplet provisioned and LAMP installed on droplet
1. ssh into droplet with command `ssh <user>@your_server_ip`

### Installing Flask:

0. Install Flask `sudo apt-get install python3-pip`  
   Install virtualenv `sudo pip install virtualenv` or `sudo apt install python3.8-venv`

1. Verify apache is working by visiting servers public ip address in browser `http://your_server_ip`

2. Install and enable mod_wsgi to enable Apache to serve Flask applications
- to Install run `sudo apt-get install libapache2-mod-wsgi-py3`  
- to enable run `sudo a2enmod wsgi`


### Deploying Flask app on Apache

1. Deploy a simple flask app
- Place app in /var/www directory using command `cd /var/www`
- Clone git repo: `sudo git clone <repo url> flaskApp/` note: replace flaskApp with name of app. Use https url
- make contents editable with `sudo chown -R $USER:$USER flaskApp/; chmod -R 777 flaskApp/`

2. Create the .wsgi file
- sudo nano flaskApp/flaskapp.wsgi
- Add the following lines of code in flaskapp.wsgi

```
#!/usr/bin/python
import sys
import logging
import os
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Flaskapp")
from Flaskapp import app as application
application.secret_key = os.urandom(32)
```

3. Creating venv
- Create venv `sudo virtualenv venv` or `sudo python3 -m venv env`
- Activate venv `source venv/bin/activate` 

4. Configure and enable New Virtual Host
- run `sudo nano /etc/apache2/sites-available/FlaskApp.conf`
- add these lines of code to the file

```
<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

- enable virtual host by running `sudo a2ensite FlaskApp`

5. Run app
- Make sure to run the correct __init__.py and all modules are installed and enabled. 

### Common Errors and Tip
- No module named flask
  `install libapache2-mod-wsgi-py3`
- View error log
  `sudo cat /var/log/apache2/error.log`
- Copying repo with app of interest
  Secure copy it into the correct location in your droplet by running `$ scp -r <AppName>/ user@droplet.ip:/var/www/<AppName>`

### Resources
* [Digital Ocean](https://www.digitalocean.com/)
* [Github Student Developer Pack](https://education.github.com/pack)
* [Deploying a flask Application on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* [Sqlite Command Line Stuff](https://sqlite.org/cli.html)



---

Accurate as of (last update): 2021-01-20

#### Contributors:
Deven Maheshwari, pd1  
Aaron Contreras, pd1  
Alejandro Alonso, pd1  
