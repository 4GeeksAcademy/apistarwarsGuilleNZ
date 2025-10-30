def add_sample_data():
    """Agregar datos de ejemplo a la base de datos"""
    try:
        from .models import User, Planet, People, db
        
        # Verificar si ya existen datos
        if User.query.first() is not None:
            print("✅ La base de datos ya contiene datos")
            return True
        
        print("📝 Insertando datos de ejemplo...")
        
        # Crear usuarios
        users = [
            User(username="lukeskywalker", email="luke@rebelalliance.com"),
            User(username="leiaorgana", email="leia@alderaan.gov"),
            User(username="hansolo", email="han@millenniumfalcon.com")
        ]
        
        for user in users:
            db.session.add(user)
        
        # Crear planetas
        planets = [
            Planet(name="Tatooine", climate="arid", terrain="desert", population="200000"),
            Planet(name="Alderaan", climate="temperate", terrain="grasslands, mountains", population="2000000000"),
            Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges", population="unknown"),
            Planet(name="Dagobah", climate="murky", terrain="swamp, jungles", population="unknown"),
            Planet(name="Endor", climate="temperate", terrain="forests, mountains, lakes", population="30000000")
        ]
        
        for planet in planets:
            db.session.add(planet)
        
        # Crear personajes
        people_list = [
            People(name="Luke Skywalker", height="172", mass="77", hair_color="blond", skin_color="fair", eye_color="blue", birth_year="19BBY", gender="male"),
            People(name="Leia Organa", height="150", mass="49", hair_color="brown", skin_color="light", eye_color="brown", birth_year="19BBY", gender="female"),
            People(name="Han Solo", height="180", mass="80", hair_color="brown", skin_color="fair", eye_color="brown", birth_year="29BBY", gender="male"),
            People(name="Darth Vader", height="202", mass="136", hair_color="none", skin_color="white", eye_color="yellow", birth_year="41.9BBY", gender="male"),
            People(name="Yoda", height="66", mass="17", hair_color="white", skin_color="green", eye_color="brown", birth_year="896BBY", gender="male")
        ]
        
        for person in people_list:
            db.session.add(person)
        
        db.session.commit()
        print("✅ Datos de ejemplo insertados correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error insertando datos: {str(e)}")
        db.session.rollback()
        return False

def get_current_user():
    """Obtener usuario actual (temporal)"""
    from .models import User
    return User.query.get(1)  # Usuario por defecto para testing