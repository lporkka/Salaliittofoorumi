from flask import Flask
app = Flask(__name__)

#database and orm
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

#login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps


def login_required(admin):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            if admin == True:
                if current_user.admin == False:
                    return login_manager.unauthorized()

            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


#load application content
from application import views
from application.posts import models, views
from application.auth import models, views
from application.threads import models, views

#login functionality, part 2
from application.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#database creation
try:
    db.create_all()
except:
    pass