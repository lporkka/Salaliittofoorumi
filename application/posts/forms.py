from flask_wtf import FlaskForm
from wtforms import StringField

class PostForm(FlaskForm):
    content = StringField("post content")

    class Meta:
        csrf = False