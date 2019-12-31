from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
workdir = os.pardir


db = SQLAlchemy()
migrate = Migrate()


def create_app(configfile="config.py"):
    from .missions.routes import mission
    from todo.missions import models
    app = Flask(__name__)
    app.config.from_pyfile(configfile)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(mission)   
    return app
