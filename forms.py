from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    '''Form for adding pet.'''

    name = StringField('Pet Name', validators=[InputRequired(
        message='Pet name cannot be blank.')])
    species = StringField('Species', validators=[InputRequired(
        message='Species cannot be blank.'), AnyOf(values=['cat', 'dog', 'porcupine'], message='Species must be either cat, dog, or porcupine.')])
    photo_url = StringField('Photo URL', validators=[
                            Optional(), URL(message='Invalid URL format.')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(
        min=0, max=30, message='Age must be between 0 and 30.')])
    notes = TextAreaField('Notes', validators=[Optional()])
