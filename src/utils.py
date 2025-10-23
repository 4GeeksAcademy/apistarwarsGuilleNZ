from src import db
from src.models import User, Planet, People, FavoritePlanet, FavoritePeople

def add_sample_data():
    """Función para agregar datos de ejemplo a la base de datos"""
    
    
    if User.query.first() is not None:
        print("⚠️  La base de datos ya contiene datos. Saltando inserción de datos de ejemplo.")
        return
    
    print("📝 Insertando datos de ejemplo...")
    
    
    users = [
        User(username="lukeskywalker", email="luke@rebelalliance.com"),
        User(username="leiaorgana", email="leia@alderaan.gov"),
        User(username="hansolo", email="han@millenniumfalcon.com")
    ]
    
    for user in users:
        db.session.add(user)
    
    
    planets = [
        Planet(name="Tatooine", climate="arid", terrain="desert", population="200000"),
        Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains", population="2000000000"),
        Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges", population="unknown"),
        Planet(name="Dagobah", climate="murky", terrain="swamp, jungles", population="unknown"),
        Planet(name="Endor", climate="temperate", terrain="forests, mountains, lakes", population="30000000"),
        Planet(name="Naboo", climate="temperate", terrain="grassy hills, swamps, forests, mountains", population="4500000000"),
        Planet(name="Coruscant", climate="temperate", terrain="cityscape, mountains", population="1000000000000")
    ]
    
    for planet in planets:
        db.session.add(planet)
    
    
    people_list = [
        People(name="Luke Skywalker", height="172", mass="77", hair_color="blond", skin_color="fair", eye_color="blue", birth_year="19BBY", gender="male"),
        People(name="Leia Organa", height="150", mass="49", hair_color="brown", skin_color="light", eye_color="brown", birth_year="19BBY", gender="female"),
        People(name="Han Solo", height="180", mass="80", hair_color="brown", skin_color="fair", eye_color="brown", birth_year="29BBY", gender="male"),
        People(name="Darth Vader", height="202", mass="136", hair_color="none", skin_color="white", eye_color="yellow", birth_year="41.9BBY", gender="male"),
        People(name="Obi-Wan Kenobi", height="182", mass="77", hair_color="auburn, white", skin_color="fair", eye_color="blue-gray", birth_year="57BBY", gender="male"),
        People(name="Yoda", height="66", mass="17", hair_color="white", skin_color="green", eye_color="brown", birth_year="896BBY", gender="male"),
        People(name="R2-D2", height="96", mass="32", hair_color="n/a", skin_color="white, blue", eye_color="red", birth_year="33BBY", gender="n/a"),
        People(name="C-3PO", height="167", mass="75", hair_color="n/a", skin_color="gold", eye_color="yellow", birth_year="112BBY", gender="n/a")
    ]
    
    for person in people_list:
        db.session.add(person)
    
    
    db.session.commit()
    print("✅ Datos de ejemplo insertados correctamente!")

def get_current_user():
    """Función para obtener el usuario actual (temporal hasta implementar autenticación)"""
    return User.query.get(1)  