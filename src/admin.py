from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src import db
from src.models import User, Planet, People, FavoritePlanet, FavoritePeople

class UserAdmin(ModelView):
    column_list = ['id', 'username', 'email', 'created_at']
    column_searchable_list = ['username', 'email']
    column_filters = ['created_at']
    form_columns = ['username', 'email']

class PlanetAdmin(ModelView):
    column_list = ['id', 'name', 'climate', 'terrain', 'population', 'created_at']
    column_searchable_list = ['name']
    column_filters = ['climate', 'terrain']
    form_columns = ['name', 'climate', 'terrain', 'population']

class PeopleAdmin(ModelView):
    column_list = ['id', 'name', 'height', 'mass', 'gender', 'birth_year']
    column_searchable_list = ['name']
    column_filters = ['gender', 'birth_year']
    form_columns = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']

class FavoritePlanetAdmin(ModelView):
    column_list = ['id', 'user', 'planet', 'created_at']
    column_filters = ['created_at']
    form_columns = ['user', 'planet']

class FavoritePeopleAdmin(ModelView):
    column_list = ['id', 'user', 'people', 'created_at']
    column_filters = ['created_at']
    form_columns = ['user', 'people']

def configure_admin(app):
    admin = Admin(app, name='StarWars Admin', template_mode='bootstrap3')
    
    
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(PlanetAdmin(Planet, db.session))
    admin.add_view(PeopleAdmin(People, db.session))
    admin.add_view(FavoritePlanetAdmin(FavoritePlanet, db.session))
    admin.add_view(FavoritePeopleAdmin(FavoritePeople, db.session))
    
    print("✅ Admin configurado correctamente")