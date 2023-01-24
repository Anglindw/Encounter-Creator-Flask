from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, PasswordField, StringField, IntegerField
from wtforms.validators import DataRequired, EqualTo


class TeamRegistry(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    tclass = SelectField('class', choices=[('fighter', 'Fighter'), ('paladin', 'Paladin'), ('wizard', 'Wizard'), ('barbarian', 'Barbarian'), ('rogue', 'Rogue') ,('cleric', 'Cleric'), ('bard', 'Bard'), ('battle dancer', 'Battle Dancer'), ('warlock', 'Warlock'), ('ranger', 'Ranger')], validate_choice=True)
    level = IntegerField('level', validators=[DataRequired()])
    submit = SubmitField()

    