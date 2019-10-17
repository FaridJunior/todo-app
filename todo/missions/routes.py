from flask import Blueprint
from flask import render_template

mission_bluprint = Blueprint("mission_blueprint", __name__, template_folder='templates')


@mission_bluprint.route("/")
@mission_bluprint.route("/home")
def index():
    return render_template('home.html', title="Home")
