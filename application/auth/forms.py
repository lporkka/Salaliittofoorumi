from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    givename = StringField("Name")
    giveusername = StringField("Username")
    givepassword = PasswordField("Password")

    class Meta:
        csrf = False
