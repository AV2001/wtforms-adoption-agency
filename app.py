from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet

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
