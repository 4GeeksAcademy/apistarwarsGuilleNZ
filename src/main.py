from flask import Blueprint, jsonify, request
from src import db
from src.models import User, Planet, People, FavoritePlanet, FavoritePeople
from src.utils import get_current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/people', methods=['GET'])
def get_all_people():
    try:
        people = People.query.all()
        return jsonify([person.serialize() for person in people]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_bp.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    try:
        person = People.query.get(people_id)
        if not person:
            return jsonify({'error': 'Personaje no encontrado'}), 404
        return jsonify(person.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_bp.route('/planets', methods=['GET'])
def get_all_planets():
    try:
        planets = Planet.query.all()
        return jsonify([planet.serialize() for planet in planets]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    try:
        planet = Planet.query.get(planet_id)
        if not planet:
            return jsonify({'error': 'Planeta no encontrado'}), 404
        return jsonify(planet.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_bp.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    try:
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        favorite_planets = FavoritePlanet.query.filter_by(user_id=current_user.id).all()
        favorite_people = FavoritePeople.query.filter_by(user_id=current_user.id).all()
        
        return jsonify({
            'favorite_planets': [fav.serialize() for fav in favorite_planets],
            'favorite_people': [fav.serialize() for fav in favorite_people]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_bp.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    try:
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        planet = Planet.query.get(planet_id)
        if not planet:
            return jsonify({'error': 'Planeta no encontrado'}), 404
        
        
        existing = FavoritePlanet.query.filter_by(
            user_id=current_user.id, 
            planet_id=planet_id
        ).first()
        if existing:
            return jsonify({'error': 'El planeta ya está en favoritos'}), 400
        
        new_favorite = FavoritePlanet(user_id=current_user.id, planet_id=planet_id)
        db.session.add(new_favorite)
        db.session.commit()
        
        return jsonify({
            'message': 'Planeta añadido a favoritos',
            'favorite': new_favorite.serialize()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main_bp.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    try:
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        person = People.query.get(people_id)
        if not person:
            return jsonify({'error': 'Personaje no encontrado'}), 404
        
        
        existing = FavoritePeople.query.filter_by(
            user_id=current_user.id, 
            people_id=people_id
        ).first()
        if existing:
            return jsonify({'error': 'El personaje ya está en favoritos'}), 400
        
        new_favorite = FavoritePeople(user_id=current_user.id, people_id=people_id)
        db.session.add(new_favorite)
        db.session.commit()
        
        return jsonify({
            'message': 'Personaje añadido a favoritos',
            'favorite': new_favorite.serialize()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main_bp.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    try:
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        favorite = FavoritePlanet.query.filter_by(
            user_id=current_user.id, 
            planet_id=planet_id
        ).first()
        
        if not favorite:
            return jsonify({'error': 'Planeta favorito no encontrado'}), 404
        
        db.session.delete(favorite)
        db.session.commit()
        
        return jsonify({'message': 'Planeta eliminado de favoritos'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main_bp.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    try:
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        favorite = FavoritePeople.query.filter_by(
            user_id=current_user.id, 
            people_id=people_id
        ).first()
        
        if not favorite:
            return jsonify({'error': 'Personaje favorito no encontrado'}), 404
        
        db.session.delete(favorite)
        db.session.commit()
        
        return jsonify({'message': 'Personaje eliminado de favoritos'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@main_bp.route('/', methods=['GET'])
def health_check():
    return jsonify({'message': 'StarWars API funcionando! 🚀'})