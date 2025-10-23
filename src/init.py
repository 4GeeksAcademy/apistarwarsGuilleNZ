from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'starwars-secret-key'
    
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    
    from src.main import main_bp
    app.register_blueprint(main_bp)
    
    
    from src.admin import configure_admin
    configure_admin(app)
    
    return app