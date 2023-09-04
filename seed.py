from app import app
from models import db, Pet

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    Pet.query.delete()

# Add data for pets
pet1 = Pet(name='Woofly', species='dog')
pet2 = Pet(name='Porchetta', species='porcupine')
pet3 = Pet(name='Snargle', species='cat')

data = [pet1, pet2, pet3]

with app.app_context():
    db.session.add_all(data)
    db.session.commit()
