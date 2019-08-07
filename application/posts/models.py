from application import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    content = db.Column(db.String, nullable=False)

    def __init__(self, content):
        self.content = content
