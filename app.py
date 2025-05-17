from flask import Flask, jsonify
from config import Config
from extentions import db  

def create_app():
    """Inicializa e configura a aplicação Flask.
    
        Responsável por:
    - Criar instância do Flask
    - Configurar extensões (SQLAlchemy)
    - Registrar blueprints
    - Criar tabelas no banco
    
    Returns:
        Flask: Aplicação configurada pronta para uso.
    """

    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        
        from routes.feiras_routes import feira_bp      
        from models.feiras import Feira
    
        db.create_all()
        app.register_blueprint(feira_bp)
    
    return app


app = create_app()
@app.route("/routes")
def list_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])


if __name__ == '__main__':
    app.run(debug=True)
