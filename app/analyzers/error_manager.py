import logging

logger = logging.getLogger(__name__)

class ErrorManager:
    @staticmethod
    def error(error_number, position=-1):
        error_messages = {
            100: f"Carácter no reconocido en posición {position}",
            400: f"Error de sintaxis en posición {position}",
            2000: "Fin inesperado del archivo"
        }
        
        message = error_messages.get(error_number, "Error desconocido")
        logger.error(f"Error {error_number}: {message}")
        return message
    
    @staticmethod
    def error_transition(state, token):
        message = f"Error en transición desde estado {state} con token {token}"
        logger.error(message)
        return message
    
    @staticmethod
    def error_final_state(state):
        message = f"Estado final: {state} (se esperaba estado de aceptación)"
        logger.error(message)
        return message