from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app(configfile="config"):
    app = Flask(__name__)
    app.config.from_pyfile(configfile)

    return app

