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

    def __init__(self, content, account_id, thread_id):
        self.content = content
        self.account_id = account_id
        self.thread_id = thread_id
