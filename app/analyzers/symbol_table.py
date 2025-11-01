from .tokens import Tokens

class Attribute:
    def __init__(self, lexeme="", token=-999, type="", value=Tokens.VACIO, state=Tokens.VACIO):
        self.lexeme = lexeme
        self.token = token
        self.type = type
        self.value = value
        self.state = state
    
    def to_dict(self):
        return {
            'lexeme': self.lexeme,
            'token': self.token,
            'type': self.type,
            'value': self.value,
            'state': self.state
        }

class SymbolTable:
    def __init__(self):
        self.table = []
    
    def insert(self, lexeme, token, type, value, state):
        attr = Attribute(lexeme, token, type, value, state)
        self.table.append(attr)
    
    def search(self, lexeme):
        for item in self.table:
            if item.lexeme == lexeme:
                return item
        return None
    
    def search_keyword(self, lexeme):
        for item in self.table:
            if item.lexeme == lexeme and item.type == "pclave":
                return item
        return None
    
    def get_lexeme_by_token(self, token):
        for item in self.table:
            if item.token == token:
                return item.lexeme
        return None
    
    def initialize_keywords(self):
        # Exactamente las mismas palabras clave que en C++
        keywords = [
            ("configuracion", Tokens.KW_SETUP), ("Configuracion", Tokens.KW_SETUP),
            ("circuito", Tokens.KW_LOOP), ("Circuito", Tokens.KW_LOOP),
            ("fin", Tokens.KW_END), ("numpin", Tokens.KW_PIN),
            ("decimal", Tokens.KW_FLOAT), ("numero", Tokens.KW_INT),
            ("salida", Tokens.SALIDA), ("entrada", Tokens.ENTRADA),
            ("si", Tokens.KW_IF), ("sino", Tokens.KW_ELSE),
            ("incluir", Tokens.INCLUIR), ("libreria", Tokens.LIBRERIA),
            ("servo", Tokens.SERVO), ("conectar", Tokens.CONECTAR),
            ("estado", Tokens.ESTADO), ("pulso", Tokens.PULSO),
            ("trigger", Tokens.TRIGGER), ("echo", Tokens.ECHO),
            ("configurar", Tokens.CONFIGURAR), ("configurar_pin", Tokens.CONFIGURAR_PIN),
            ("encender", Tokens.ENCENDER), ("apagar", Tokens.APAGAR),
            ("esperar", Tokens.ESPERAR), ("leer_sensor", Tokens.LEER_SENSOR),
            ("intensidad", Tokens.INTENSIDAD), ("for", Tokens.KW_FOR),
            ("veces", Tokens.KW_TIME)
        ]
        
        # Delimitadores y operadores (igual que en C++)
        operators = [
            ("=", Tokens.IGUAL), (";", Tokens.PCOMA), (",", Tokens.COMA),
            ("(", Tokens.APARENTESIS), (")", Tokens.CPARENTESIS),
            (":", Tokens.DOSPUNTOS), (">", Tokens.MAYOR), ("<", Tokens.MENOR),
            ("+", Tokens.MAS), ("-", Tokens.MENOS), ("*", Tokens.POR),
            ("/", Tokens.DIVIDIDO), (".", Tokens.PUNTO), ("#", Tokens.COMENTARIO)
        ]
        
        for lexeme, token in keywords + operators:
            self.insert(lexeme, token, "pclave", Tokens.VACIO, Tokens.VACIO)
    
    def to_dict(self):
        return [item.to_dict() for item in self.table]