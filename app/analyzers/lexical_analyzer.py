from .tokens import Tokens

class LexicalAnalyzer:
    def __init__(self, code, symbol_table):
        self.code = code
        self.symbol_table = symbol_table
        self.position = 0
        self.current_variable = ""
        self.current_number = ""
        self.current_string = ""
        self.tokens = Tokens()  # Instancia de Tokens para acceder a las constantes
    
    def is_element(self, char):
        elements = "(){}=,;.'\":><+-*/"
        return char in elements
    
    def get_token(self):
        # Saltar espacios en blanco
        while self.position < len(self.code) and self.code[self.position] in ' \n\t\r':
            self.position += 1
        
        # Fin de archivo
        if self.position >= len(self.code):
            return Tokens.FIN_ARCHIVO
        
        # Comentarios
        if self.code[self.position] == '#':
            while (self.position < len(self.code) and 
                   self.code[self.position] != '\n' and 
                   self.code[self.position] != '\0'):
                self.position += 1
            return Tokens.COMENTARIO
        
        # Cadenas entre comillas
        if self.code[self.position] == '"':
            self.position += 1
            string_content = ""
            while (self.position < len(self.code) and 
                   self.code[self.position] != '"' and 
                   self.code[self.position] != '\0'):
                string_content += self.code[self.position]
                self.position += 1
            
            if (self.position < len(self.code) and self.code[self.position] == '"'):
                self.position += 1
            
            self.current_string = string_content
            return Tokens.CADENA
        
        # Identificadores y palabras clave
        if self.code[self.position].isalpha() or self.code[self.position] == '_':
            identifier = ""
            while (self.position < len(self.code) and 
                   (self.code[self.position].isalnum() or self.code[self.position] == '_')):
                identifier += self.code[self.position]
                self.position += 1
            
            keyword = self.symbol_table.search_keyword(identifier)
            if keyword:
                return keyword.token
            
            self.current_variable = identifier
            return Tokens.VAR
        
        # Números
        if self.code[self.position].isdigit():
            number = ""
            has_point = False
            while (self.position < len(self.code) and 
                   (self.code[self.position].isdigit() or self.code[self.position] == '.')):
                if self.code[self.position] == '.':
                    if has_point:
                        break
                    has_point = True
                number += self.code[self.position]
                self.position += 1
            
            self.current_number = number
            return Tokens.NUM
        
        # Delimitadores y operadores
        if self.is_element(self.code[self.position]):
            char = self.code[self.position]
            self.position += 1
            
            keyword = self.symbol_table.search_keyword(char)
            if keyword:
                return keyword.token
            
            return Tokens.ERROR_TOKEN
        
        # Carácter no reconocido
        self.position += 1
        return Tokens.ERROR_TOKEN
    
    def analyze(self):
        self.position = 0
        tokens = []
        errors = []
        
        try:
            while True:
                token = self.get_token()
                
                if token == Tokens.FIN_ARCHIVO:
                    tokens.append({
                        'token': token,
                        'value': 'EOF',
                        'type': 'eof'
                    })
                    break
                elif token == Tokens.ERROR_TOKEN:
                    errors.append(f"Carácter no reconocido en posición {self.position}")
                    break
                elif token == Tokens.VAR:
                    if not self.symbol_table.search(self.current_variable):
                        self.symbol_table.insert(
                            self.current_variable, Tokens.VAR, 
                            "variable", Tokens.VACIO, Tokens.VACIO
                        )
                    tokens.append({
                        'token': token,
                        'value': self.current_variable,
                        'type': 'variable'
                    })
                elif token == Tokens.NUM:
                    tokens.append({
                        'token': token,
                        'value': self.current_number,
                        'type': 'number'
                    })
                elif token == Tokens.CADENA:
                    tokens.append({
                        'token': token,
                        'value': self.current_string,
                        'type': 'string'
                    })
                elif token == Tokens.COMENTARIO:
                    tokens.append({
                        'token': token,
                        'value': 'comment',
                        'type': 'comment'
                    })
                else:
                    tokens.append({
                        'token': token,
                        'value': f'token_{token}',
                        'type': 'keyword'
                    })
        except Exception as e:
            errors.append(f"Error durante análisis léxico: {str(e)}")
        
        return {
            'success': len(errors) == 0,
            'tokens': tokens,
            'errors': errors,
            'symbol_table': self.symbol_table.to_dict()
        }
    
    def reiniciar(self):
        self.position = 0