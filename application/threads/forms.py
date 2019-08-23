from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ThreadForm(FlaskForm):
    header = StringField("Header", [validators.length(min=1)])
    content = StringField("Content", [validators.length(min=1)])

    class Meta:
        csrf = False