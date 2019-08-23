from application import db
from application.models import Base


class Post(Base):
    __tablename__ = "post"

    content = db.Column(db.String, nullable=False)
    account_id = db.Column(db.Integer,
                           db.ForeignKey('account.id'),
                           nullable=False)
    thread_id = db.Column(db.Integer,
                          db.ForeignKey('thread.id'),
                          nullable=False)

    def __init__(self, content):
        self.content = content
