from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def configure_admin(app):
    from .models import User, Planet, People, FavoritePlanet, FavoritePeople, db
    
    admin = Admin(app, name='StarWars API Admin', template_mode='bootstrap3')
    
    class UserModelView(ModelView):
        column_list = ['id', 'username', 'email', 'created_at']
        column_searchable_list = ['username', 'email']
    
    class PlanetModelView(ModelView):
        column_list = ['id', 'name', 'climate', 'terrain', 'population']
        column_searchable_list = ['name']
    
    class PeopleModelView(ModelView):
        column_list = ['id', 'name', 'height', 'mass', 'gender', 'birth_year']
        column_searchable_list = ['name']
    
    class FavoritePlanetModelView(ModelView):
        column_list = ['id', 'user_id', 'planet_id', 'created_at']
    
    class FavoritePeopleModelView(ModelView):
        column_list = ['id', 'user_id', 'people_id', 'created_at']
    
    # Agregar vistas
    admin.add_view(UserModelView(User, db.session, name='Usuarios'))
    admin.add_view(PlanetModelView(Planet, db.session, name='Planetas'))
    admin.add_view(PeopleModelView(People, db.session, name='Personajes'))
    admin.add_view(FavoritePlanetModelView(FavoritePlanet, db.session, name='Favoritos Planetas'))
    admin.add_view(FavoritePeopleModelView(FavoritePeople, db.session, name='Favoritos Personajes'))