from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "message": "StarWars API funcionando! 🚀",
        "status": "active",
        "endpoints": {
            "people": "/people",
            "planets": "/planets", 
            "users": "/users",
            "favorites": "/users/favorites"
        }
    })

# El resto de los endpoints se mantienen igual...
# [Aquí van todos los demás endpoints que ya tenías]