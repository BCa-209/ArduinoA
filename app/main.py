#!/usr/bin/env python3
"""
Módulo principal de la aplicación Flask
"""
import os
import logging
from app import create_app

logger = logging.getLogger(__name__)

def main():
    """Función principal para iniciar la aplicación local"""
    try:
        # Crear aplicación Flask
        app = create_app()
        
        # Configuración para desarrollo local
        host = '127.0.0.1'
        port = 5000
        debug = True
        
        print("🎯 Iniciando servidor de desarrollo...")
        print(f"🌐 Accede en: http://{host}:{port}")
        print("🛑 Para detener: Ctrl + C")
        print("-" * 50)
        
        # Iniciar servidor de desarrollo Flask
        app.run(
            host=host, 
            port=port, 
            debug=debug,
            use_reloader=True
        )
        
    except Exception as e:
        logger.error(f"Error al iniciar la aplicación: {str(e)}")
        print(f"❌ Error: {str(e)}")