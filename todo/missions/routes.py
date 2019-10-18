from flask import Blueprint
from flask import redirect, url_for
from flask import render_template

from .forms import NewMission, UpdateMission
from .models import Mission, db

mission = Blueprint("mission", __name__, template_folder='templates')


@mission.route("/")
@mission.route("/home")
def home():
    return render_template('home.html', title="Home")


@mission.route("/add", methods=['POST', 'GET'])
def add_mission():
    form = NewMission()
    if form.validate_on_submit():
        mission = Mission(content=form.content.data)
        db.session.add(mission)
        db.session.commit()
        return redirect(url_for('mission.list_missions'))
    return render_template('add_mission.html', title="Add Mission", form=form)


@mission.route("/list")
def list_missions():
    missions = Mission.query.order_by(Mission.id.desc()).filter(Mission.done == False).all()
    return render_template('list_mission.html', title="List Mission", missions=missions)


@mission.route("/done/list")
def done_missions():
    missions = Mission.query.filter(Mission.done == True).all()
    return render_template('done_mission.html', title="done Mission", missions=missions)


# action in mission
@mission.route('/mission/done/<int:id>')
def mission_done(id):
    mission = Mission.query.get(id)
    if mission:
        mission.done = True
    db.session.commit()
    return redirect(url_for('mission.done_missions'))


@mission.route('/mission/delete/<int:id>')
def mission_delete(id):
    mission = Mission.query.get(id)
    if mission:
        db.session.delete(mission)
    db.session.commit()
    return redirect(url_for('mission.list_missions'))


@mission.route("/update/<int:id>", methods=['POST', 'GET'])
def mission_update(id):
    form = UpdateMission()
    mission = Mission.query.get_or_404(id)
    if form.validate_on_submit():
        mission.content = form.content.data
        db.session.commit()
        return redirect(url_for('mission.list_missions'))
    else:
        form.content.data = mission.content
    return render_template('update_mission.html', title="Add Mission", form=form, mission=mission)


@mission.route('/mission/undo/<int:id>')
def mission_undo(id):
    mission = Mission.query.get_or_404(id)
    if mission:
        mission.done = False
    db.session.commit()
    return redirect(url_for('mission.list_missions'))
