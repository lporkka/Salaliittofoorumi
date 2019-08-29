from application import db
from application.models import Base


class Topic(Base):
    __tablename__ = "topic"

    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name
