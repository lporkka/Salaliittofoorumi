from application import db
from application.models import Base

from sqlalchemy.sql import text


class Thread(Base):
    __tablename__ = "thread"

    header = db.Column(db.String, nullable=False)
    posts = db.relationship("Post", backref='thread', lazy=True)

    def __init__(self, header):
        self.header = header

    @staticmethod
    def find_by_name(header):
        stmt = text("SELECT thread.id FROM thread "
                    "WHERE thread.header = :header").params(header=header)
        res = db.engine.execute(stmt).fetchone()
        return res[0]