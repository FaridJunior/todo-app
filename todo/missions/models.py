from todo import db , login
from flask_login import UserMixin  
from werkzeug.security import generate_password_hash , check_password_hash
from  datetime import datetime

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Mission {}>'.format(self.content)
