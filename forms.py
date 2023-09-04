from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    '''Form for adding pet.'''

    name = StringField('Pet Name', validators=[InputRequired(
        message='Pet name cannot be blank.')])
    species = SelectField('Species', choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[
                            Optional(), URL(message='Invalid URL format.')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(
        min=0, max=30, message='Age must be between 0 and 30.')])
    notes = TextAreaField('Notes', validators=[Optional()])
