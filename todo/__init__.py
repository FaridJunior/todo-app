from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .missions.routes import mission_bluprint

db = SQLAlchemy()


def create_app(configfile="config"):
    app = Flask(__name__)
    app.config.from_pyfile(configfile)
    db.init_app(app)
    app.register_blueprint(mission_bluprint)
    with app.app_context():
        db.create_all()
        return app
    return app
