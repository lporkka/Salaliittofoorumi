from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    givename = StringField("Name", render_kw=dict(autocomplete=False))
    giveusername = StringField("Username", render_kw=dict(autocomplete=False))
    givepassword = PasswordField("Password",
                                 render_kw=dict(autocomplete=False))

    class Meta:
        csrf = False
