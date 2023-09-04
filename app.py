from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet
from forms import AddPetForm

# Create new instance of Flask application.
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'eufo3gf23fo'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


db.init_app(app)


# Routes
@app.route('/')
def home_page():
    '''List all pets.'''
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Add a pet to the database.'''
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else 'https://shorturl.at/nuNX3'
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)
