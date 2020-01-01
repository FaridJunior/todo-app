from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField
from wtforms.validators import DataRequired ,ValidationError
from .models import User

class NewMission(FlaskForm):
    content = TextAreaField('Mission', validators=[DataRequired()])
    submit = SubmitField('Add')

    


class UpdateMission(FlaskForm):
    content = TextAreaField('Mission', validators=[DataRequired()])
    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
class RegisterForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def Validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if  user is not None:
            raise ValidationError('use another user name')