from src import create_app, db
from src.utils import add_sample_data

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Comando para inicializar la base de datos"""
    print("🗃️  Creando tablas de la base de datos...")
    db.drop_all()
    db.create_all()
    
    print("📝 Agregando datos de ejemplo...")
    add_sample_data()
    
    print("✅ Base de datos inicializada correctamente!")

if __name__ == '__main__':
    with app.app_context():
        
        db.create_all()
        
        add_sample_data()
    
    print("🚀 Iniciando StarWars API en http://localhost:3001")
    print("📊 Panel de admin en http://localhost:3001/admin")
    app.run(host='0.0.0.0', port=3001, debug=True)