from .tokens import Tokens

class SyntaxAutomata:
    def __init__(self):
        self.state = 0
        self.transition_table = {}
        self.final_states = {21, 52}  # Estados finales aceptables
        self.initialize_transitions()
    
    def initialize_transitions(self):
        # Estado 0: Inicio
        self.transition_table[(0, Tokens.KW_SETUP)] = 1
        self.transition_table[(0, Tokens.INCLUIR)] = 50
        self.transition_table[(0, Tokens.COMENTARIO)] = 0
        self.transition_table[(0, Tokens.FIN_ARCHIVO)] = 21
        
        # Estado 1: Después de KW_SETUP
        self.transition_table[(1, Tokens.DOSPUNTOS)] = 2
        
        # Estado 2: Después de ':' en SETUP
        self.transition_table[(2, Tokens.KW_PIN)] = 3
        self.transition_table[(2, Tokens.KW_FLOAT)] = 3
        self.transition_table[(2, Tokens.KW_INT)] = 3
        self.transition_table[(2, Tokens.CONFIGURAR)] = 12
        self.transition_table[(2, Tokens.KW_END)] = 7
        
        # Estados para declaración de pines con números
        self.transition_table[(3, Tokens.VAR)] = 4
        self.transition_table[(3, Tokens.NUM)] = 4  # Añadir transición para NUM
        
        self.transition_table[(4, Tokens.VAR)] = 5
        self.transition_table[(5, Tokens.IGUAL)] = 6
        self.transition_table[(5, Tokens.PCOMA)] = 2
        
        # Estados para asignación de valores (incluyendo números)
        self.transition_table[(6, Tokens.NUM)] = 2  # Permitir números como valores
        self.transition_table[(6, Tokens.VAR)] = 2
        self.transition_table[(6, Tokens.LEER_SENSOR)] = 23
        
        # Estados para configuración de pines con números
        self.transition_table[(12, Tokens.APARENTESIS)] = 13
        self.transition_table[(13, Tokens.VAR)] = 14
        self.transition_table[(13, Tokens.NUM)] = 14  # Añadir transición para NUM
        
        self.transition_table[(14, Tokens.COMA)] = 15
        self.transition_table[(15, Tokens.SALIDA)] = 16
        self.transition_table[(15, Tokens.ENTRADA)] = 16
        
        self.transition_table[(16, Tokens.CPARENTESIS)] = 17
        self.transition_table[(17, Tokens.PCOMA)] = 2
        
        # Estado 7: Después de KW_END en SETUP
        self.transition_table[(7, Tokens.KW_LOOP)] = 8
        
        # Estado 8: Después de KW_LOOP
        self.transition_table[(8, Tokens.DOSPUNTOS)] = 9
        
        # Estado 9: LOOP principal
        self.transition_table[(9, Tokens.APAGAR)] = 11
        self.transition_table[(9, Tokens.ENCENDER)] = 11
        self.transition_table[(9, Tokens.ESPERAR)] = 11
        self.transition_table[(9, Tokens.KW_FLOAT)] = 10
        self.transition_table[(9, Tokens.KW_INT)] = 10
        self.transition_table[(9, Tokens.KW_FOR)] = 26
        self.transition_table[(9, Tokens.KW_IF)] = 26
        self.transition_table[(9, Tokens.KW_END)] = 21  # Permitir END para terminar
        self.transition_table[(9, Tokens.FIN_ARCHIVO)] = 21
        
        # Estados para funciones en LOOP con números
        self.transition_table[(10, Tokens.VAR)] = 17
        self.transition_table[(17, Tokens.IGUAL)] = 22
        self.transition_table[(11, Tokens.APARENTESIS)] = 18
        self.transition_table[(18, Tokens.VAR)] = 19
        self.transition_table[(18, Tokens.NUM)] = 19  # Añadir transición para NUM
        
        self.transition_table[(19, Tokens.CPARENTESIS)] = 20
        self.transition_table[(20, Tokens.PCOMA)] = 9
        
        # Estados para operaciones matemáticas
        self.transition_table[(22, Tokens.LEER_SENSOR)] = 23
        self.transition_table[(22, Tokens.VAR)] = 24
        self.transition_table[(22, Tokens.NUM)] = 23  # Permitir números directos
        
        self.transition_table[(23, Tokens.PCOMA)] = 9
        self.transition_table[(24, Tokens.POR)] = 25
        self.transition_table[(24, Tokens.MAS)] = 25
        self.transition_table[(24, Tokens.MENOS)] = 25
        self.transition_table[(25, Tokens.NUM)] = 23
        self.transition_table[(25, Tokens.VAR)] = 23
        
        # Estados para estructuras de control
        self.transition_table[(26, Tokens.APARENTESIS)] = 27
        self.transition_table[(27, Tokens.VAR)] = 28
        
        self.transition_table[(28, Tokens.IGUAL)] = 29
        self.transition_table[(28, Tokens.MAYOR)] = 29
        self.transition_table[(28, Tokens.MENOR)] = 29
        
        self.transition_table[(29, Tokens.VAR)] = 30
        self.transition_table[(29, Tokens.NUM)] = 30  # Añadir transición para NUM
        
        self.transition_table[(30, Tokens.CPARENTESIS)] = 31
        self.transition_table[(31, Tokens.PCOMA)] = 9
        
        # Estados para incluir librerías
        self.transition_table[(50, Tokens.LIBRERIA)] = 51
        self.transition_table[(51, Tokens.CADENA)] = 52
        self.transition_table[(52, Tokens.PCOMA)] = 0
    
    def transition(self, token):
        key = (self.state, token)
        
        # DEBUG: Mostrar transición intentada
        # print(f"DEBUG: Estado {self.state}, Token {token}")
        
        if key in self.transition_table:
            self.state = self.transition_table[key]
            # print(f"DEBUG: Transición exitosa a estado {self.state}")
            return token
        else:
            # Tokens que permiten permanecer en el estado actual o ignorar
            if token == Tokens.COMENTARIO:
                # Comentarios no afectan el estado
                return token
            
            if token == Tokens.FIN_ARCHIVO:
                # EOF es aceptable en varios estados
                if self.state in [0, 2, 9, 21, 52]:
                    self.state = 21
                    return token
            
            # Si no hay transición definida, error
            # print(f"DEBUG: ERROR - No hay transición desde estado {self.state} con token {token}")
            return Tokens.ERROR_TOKEN
    
    def is_final_state(self):
        return self.state in self.final_states
    
    def reset(self):
        self.state = 0
    
    def get_state(self):
        return self.state
