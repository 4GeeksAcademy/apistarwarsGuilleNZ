import os
import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Configuración básica de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'starwars-secret-key'

db = SQLAlchemy(app)
CORS(app)

# Modelos básicos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    population = db.Column(db.String(100))

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(50))
    mass = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))

class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)

class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)

# Endpoints básicos
@app.route('/')
def home():
    return jsonify({"message": "StarWars API funcionando! 🚀"})

@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'height': p.height,
        'mass': p.mass,
        'hair_color': p.hair_color,
        'skin_color': p.skin_color,
        'eye_color': p.eye_color,
        'birth_year': p.birth_year,
        'gender': p.gender
    } for p in people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
    if not person:
        return jsonify({'error': 'Personaje no encontrado'}), 404
    return jsonify({
        'id': person.id,
        'name': person.name,
        'height': person.height,
        'mass': person.mass,
        'hair_color': person.hair_color,
        'skin_color': person.skin_color,
        'eye_color': person.eye_color,
        'birth_year': person.birth_year,
        'gender': person.gender
    })

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'climate': p.climate,
        'terrain': p.terrain,
        'population': p.population
    } for p in planets])

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    try:
        # Usuario temporal (ID 1)
        user = User.query.get(1)
        if not user:
            user = User(username="default", email="default@example.com")
            db.session.add(user)
            db.session.commit()
        
        person = People.query.get(people_id)
        if not person:
            return jsonify({'error': 'Personaje no encontrado'}), 404
        
        # Verificar si ya es favorito
        existing = FavoritePeople.query.filter_by(user_id=1, people_id=people_id).first()
        if existing:
            return jsonify({'error': 'Ya está en favoritos'}), 400
        
        favorite = FavoritePeople(user_id=1, people_id=people_id)
        db.session.add(favorite)
        db.session.commit()
        
        return jsonify({
            'message': 'Personaje añadido a favoritos',
            'people_id': people_id,
            'name': person.name
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users/favorites', methods=['GET'])
def get_favorites():
    favorites_people = FavoritePeople.query.filter_by(user_id=1).all()
    result = []
    for fav in favorites_people:
        person = People.query.get(fav.people_id)
        if person:
            result.append({
                'id': person.id,
                'name': person.name,
                'height': person.height,
                'mass': person.mass
            })
    return jsonify({'favorites': result})

# Función para datos de ejemplo
def add_sample_data():
    if People.query.first() is None:
        # Agregar personajes de ejemplo
        characters = [
            People(name="Luke Skywalker", height="172", mass="77", hair_color="blond", skin_color="fair", eye_color="blue", birth_year="19BBY", gender="male"),
            People(name="Leia Organa", height="150", mass="49", hair_color="brown", skin_color="light", eye_color="brown", birth_year="19BBY", gender="female"),
            People(name="Han Solo", height="180", mass="80", hair_color="brown", skin_color="fair", eye_color="brown", birth_year="29BBY", gender="male")
        ]
        for char in characters:
            db.session.add(char)
        
        # Agregar planetas de ejemplo
        planets = [
            Planet(name="Tatooine", climate="arid", terrain="desert", population="200000"),
            Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains", population="2000000000")
        ]
        for planet in planets:
            db.session.add(planet)
        
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_sample_data()
    
    print("🚀 StarWars API iniciada en http://localhost:3000")
    app.run(host='0.0.0.0', port=3000, debug=True)