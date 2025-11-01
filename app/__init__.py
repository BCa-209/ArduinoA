from flask import Flask
import os

def create_app():
    # Obtener la ruta absoluta del directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)  # Subir un nivel a ArduinoA/
    
    app = Flask(__name__, 
                template_folder=os.path.join(project_root, 'templates'),
                static_folder=os.path.join(project_root, 'static'))
    
    # Configuración básica
    app.config['SECRET_KEY'] = 'dev-secret-key-local'
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app