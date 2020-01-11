from flask import Blueprint
from flask import redirect, url_for, flash
from flask import render_template
from .models import db , User
from .forms import LoginForm, RegisterForm
from flask_login import current_user , login_user , logout_user
user = Blueprint("user", __name__ , template_folder='templates')


@user.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('list_missions'))
    if form.validate_on_submit():
        user = User(username = form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user)
        return redirect(url_for('mission.add_mission'))
    return render_template('register.html', form =form)



@user.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('list_missions'))
    if form.validate_on_submit():
        user =  User.query.filter_by(username= form.username.data).first()
        if user is not None and  user.check_password(form.username.data) is not False:
            flash('user login')
            login_user(user,remember=form.remember.data)
            return redirect(url_for('mission.add_mission'))
        else :
            flash("please enter true user name and pass")
            return redirect(url_for('user.login'))
    return render_template('login.html', form =form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))