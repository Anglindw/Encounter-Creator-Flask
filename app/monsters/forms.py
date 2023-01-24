from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class ApiMonster(FlaskForm):
    entry = StringField('entry', validators=[DataRequired()])
    submit = SubmitField()

class CustomMonster(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    challenge_rating = IntegerField('challenge_rating', validators=[DataRequired()])
    

