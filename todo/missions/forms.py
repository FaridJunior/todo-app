from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField
from wtforms.validators import DataRequired ,ValidationError
class NewMission(FlaskForm):
    content = TextAreaField('Mission', validators=[DataRequired()])
    submit = SubmitField('Add')

    


class UpdateMission(FlaskForm):
    content = TextAreaField('Mission', validators=[DataRequired()])
    submit = SubmitField('Update')