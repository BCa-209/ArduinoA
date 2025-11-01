class AnalysisResult:
    def __init__(self, lexical_result, syntax_result, symbol_table):
        self.lexical_result = lexical_result
        self.syntax_result = syntax_result
        self.symbol_table = symbol_table
        # Calcular el éxito general
        self.overall_success = lexical_result['success'] and syntax_result['success']
    
    def to_dict(self):
        return {
            'lexical_analysis': self.lexical_result,
            'syntax_analysis': self.syntax_result,
            'symbol_table': self.symbol_table.to_dict() if hasattr(self.symbol_table, 'to_dict') else [],
            'overall_success': self.overall_success
        }