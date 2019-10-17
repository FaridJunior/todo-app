from flask import  render_template
from flask import Blueprint

mission_bluprint = Blueprint("mission_blueprint", __name__, template_folder='templates')


@mission_bluprint.route("/")
def index():
    return render_template('home.html')