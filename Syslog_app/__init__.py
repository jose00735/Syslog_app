from flask import Flask
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2f24ab45ab5abbed3857b751b903bbc7'
bcrypt = Bcrypt(app)

from Syslog_app import routes
