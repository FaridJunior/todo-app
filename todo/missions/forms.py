from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired



class NewMission(FlaskForm):
    content = TextAreaField('Mission', validators=[DataRequired()])
    submit = SubmitField('Add')


class UpdateMission(FlaskForm):
    content = TextAreaField('Mission', validators=[DataRequired()])
    submit = SubmitField('Update')
