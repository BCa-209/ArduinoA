# Tokens para el lenguaje de sistemas embebidos
class Tokens:
    # Palabras reservadas
    KW_SETUP = 1
    KW_LOOP = 2
    KW_END = 3
    KW_PIN = 4
    KW_FLOAT = 5
    KW_INT = 6
    SALIDA = 7
    CONFIGURAR = 8
    ENCENDER = 9
    APAGAR = 10
    ESPERAR = 11
    KW_FOR = 12
    KW_TIME = 13
    KW_IF = 14
    KW_ELSE = 15
    LEER_SENSOR = 16
    INTENSIDAD = 17
    CONFIGURAR_PIN = 18
    
    # Nuevos tokens
    INCLUIR = 35
    LIBRERIA = 36
    ENTRADA = 37
    SERVO = 38
    CONECTAR = 39
    ESTADO = 40
    PULSO = 41
    TRIGGER = 42
    ECHO = 43
    PUNTO = 44
    
    # Operadores y delimitadores
    IGUAL = 19
    PCOMA = 20
    COMA = 21
    APARENTESIS = 22
    CPARENTESIS = 23
    DOSPUNTOS = 24
    MAYOR = 25
    MENOR = 26
    MAS = 27
    MENOS = 28
    POR = 29
    DIVIDIDO = 30
    
    # Identificadores y literales
    VAR = 31
    NUM = 32
    CADENA = 33
    COMENTARIO = 34
    
    FIN_ARCHIVO = 666
    ERROR_TOKEN = 999
    
    # Constantes
    NULL = "NULL"
    VACIO = "-"
    ASIGNADO = "asignado"