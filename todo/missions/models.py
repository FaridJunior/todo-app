from todo import db

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text)
    done = db.Column(db.Boolean, nullable=False, default=False)
