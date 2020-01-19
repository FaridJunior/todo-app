from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(configfile="config.py"):
    app = Flask(__name__)
    from .missions.routes import mission
    from .users.routes import user
    from .errors import handler
    from todo.missions import models
    app.config.from_pyfile(configfile)
    db.init_app(app)
    login.init_app(app)
    login.login = 'user.login'
    migrate.init_app(app, db)


    app.register_blueprint(mission)
    app.register_blueprint(user)
    app.register_blueprint(handler.error)  

    return app
