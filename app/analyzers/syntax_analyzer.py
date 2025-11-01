from .automata import SyntaxAutomata
from .tokens import Tokens

class SyntaxAnalyzer:
    def __init__(self, lexical_analyzer, symbol_table):
        self.lexical_analyzer = lexical_analyzer
        self.symbol_table = symbol_table
        self.automata = SyntaxAutomata()
    
    def analyze(self):
        self.lexical_analyzer.reiniciar()
        self.automata.reset()
        
        tokens_processed = 0
        errors = []
        
        try:
            while True:
                token = self.lexical_analyzer.get_token()
                
                if token == Tokens.FIN_ARCHIVO:
                    break
                
                if token == Tokens.ERROR_TOKEN:
                    errors.append("Token de error encontrado en análisis léxico")
                    break
                
                # Realizar transición de manera segura
                result = self.automata.transition(token)
                tokens_processed += 1
                
                if result == Tokens.ERROR_TOKEN:
                    errors.append(f"Error sintáctico en token {token} (posición {tokens_processed})")
                    # Continuar analizando en lugar de romper
                    # break
            
            # Verificar estado final
            if not self.automata.is_final_state():
                errors.append(f"Estado final no aceptable: {self.automata.get_state()}")
            
        except Exception as e:
            errors.append(f"Error durante análisis sintáctico: {str(e)}")
        
        return {
            'success': len(errors) == 0,
            'errors': errors,
            'final_state': self.automata.get_state(),
            'tokens_processed': tokens_processed
        }