from application import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

	header = db.Column(db.String(144), nullable=False)
	content = db.Column(db.String, nullable=False)
	
	def __init__(self, header, content):
		self.header = header
		self.content = content
