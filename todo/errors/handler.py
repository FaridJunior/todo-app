from flask import render_template, Blueprint
from .. import db

error = Blueprint('errors' ,__name__)

@error.app_errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

@error.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("500.html"), 500


@error.app_errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401
