#!/usr/bin/env python3
"""
ANALIZADOR DE LENGUAJE PARA SISTEMAS EMBEBIDOS
Punto de entrada principal - Versión Local
"""
import os
import logging
from app.main import main

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 ANALIZADOR DE LENGUAJE EMBEBIDOS")
    print("📍 URL: http://127.0.0.1:5000")
    print("=" * 60)
    main()