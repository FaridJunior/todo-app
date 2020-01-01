from todo import db
from flask_login import UserMixin


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Mission {}>'.format(self.content)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60),unique=True, nullable=False)
    missions = db.relationship('Mission', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User {}>'.format(self.username)


