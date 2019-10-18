from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(configfile="config"):
    from .missions.routes import mission
    from todo.missions import models
    app = Flask(__name__)
    app.config.from_pyfile(configfile)
    db.init_app(app)
    app.register_blueprint(mission)
    with app.app_context():
        db.create_all()
        return app
    return app
