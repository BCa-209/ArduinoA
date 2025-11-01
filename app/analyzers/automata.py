from .tokens import Tokens

class SyntaxAutomata:
    def __init__(self):
        self.state = 0
        # Crear una tabla de transiciones más segura
        self.transition_table = {}
        self.initialize_transitions()
    
    def initialize_transitions(self):
        # Usar diccionario en lugar de lista para evitar índices fuera de rango
        # Estado 0: Inicio
        self.transition_table[(0, Tokens.KW_SETUP)] = 1
        self.transition_table[(0, Tokens.INCLUIR)] = 50
        self.transition_table[(0, Tokens.KW_LOOP)] = 4
        self.transition_table[(0, Tokens.COMENTARIO)] = 0
        self.transition_table[(0, Tokens.FIN_ARCHIVO)] = 23
        
        # Configuración básica
        self.transition_table[(1, Tokens.DOSPUNTOS)] = 2
        self.transition_table[(2, Tokens.KW_PIN)] = 3
        self.transition_table[(3, Tokens.NUM)] = 4
        self.transition_table[(4, Tokens.VAR)] = 5
        self.transition_table[(5, Tokens.SALIDA)] = 6
        self.transition_table[(5, Tokens.ENTRADA)] = 6
        self.transition_table[(6, Tokens.PCOMA)] = 2
        self.transition_table[(2, Tokens.KW_END)] = 7
        
        # Estados finales
        self.final_states = {7, 13, 23, 52}
    
    def transition(self, token):
        key = (self.state, token)
        
        if key in self.transition_table:
            self.state = self.transition_table[key]
            return token
        else:
            # Si no hay transición, permanecer en el estado actual para algunos tokens
            if token in [Tokens.COMENTARIO, Tokens.FIN_ARCHIVO]:
                return token
            return Tokens.ERROR_TOKEN
    
    def is_final_state(self):
        return self.state in self.final_states
    
    def reset(self):
        self.state = 0
    
    def get_state(self):
        return self.state