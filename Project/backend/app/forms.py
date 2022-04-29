from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    playername = StringField('Playername', validators=[DataRequired()])
    team = StringField('team', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    month = StringField('month', validators=[DataRequired()])
    date = StringField('date', validators=[DataRequired()])
    submit = SubmitField('Submit')