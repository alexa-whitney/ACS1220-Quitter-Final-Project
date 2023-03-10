from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from quitter_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# Authentication Setup Code
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

bcrypt = Bcrypt(app)

###########################
# Main
###########################

#  Main Blueprint

from quitter_app.main.routes import main
app.register_blueprint(main)

with app.app_context(): 
    db.create_all()

# Auth Blueprint
from quitter_app.auth.routes import auth
app.register_blueprint(auth)

with app.app_context(): 
    db.create_all()