from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    '''Form for adding pet.'''

    name = StringField('Pet Name', validators=[InputRequired(
        message='Pet name cannot be blank.')])
    species = StringField('Species', validators=[InputRequired(
        message='Species cannot be blank.')])
    photo_url = StringField('Photo URL', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
