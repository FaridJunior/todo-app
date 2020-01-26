from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_moment import Moment
import logging
from logging.handlers import SMTPHandler





db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
moment = Moment()
def create_app(configfile="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(configfile)
    
    from .missions.routes import mission
    from .users.routes import user
    from .errors import handler
    from todo.missions import models
    
    db.init_app(app)
    moment.init_app(app)
    login.init_app(app)
    login.login = 'user.login'
    migrate.init_app(app, db)

    app.register_blueprint(mission)
    app.register_blueprint(user)
    app.register_blueprint(handler.error)
    handle_email_log(app)
    return app

def handle_email_log(app):
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'], subject=' Todo Failure',
        credentials=auth, secure=secure
        )
    
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    if not app.debug:
        app.logger.addHandler(mail_handler)