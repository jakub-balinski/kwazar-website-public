from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from kwazar_website.config import Config
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.session_protection = "strong"
mail = Mail(app)
cors = CORS(app)

from kwazar_website import routes
