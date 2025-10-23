from src import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    favorite_planets = db.relationship('FavoritePlanet', backref='user', lazy=True, cascade='all, delete-orphan')
    favorite_people = db.relationship('FavoritePeople', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    population = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    favorites = db.relationship('FavoritePlanet', backref='planet', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population
        }

class People(db.Model):
    __tablename__ = 'people'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(50))
    mass = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    favorites = db.relationship('FavoritePeople', backref='people', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year,
            'gender': self.gender
        }

class FavoritePlanet(db.Model):
    __tablename__ = 'favorite_planet'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'planet_id': self.planet_id,
            'planet_name': self.planet.name if self.planet else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class FavoritePeople(db.Model):
    __tablename__ = 'favorite_people'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'people_id': self.people_id,
            'people_name': self.people.name if self.people else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }