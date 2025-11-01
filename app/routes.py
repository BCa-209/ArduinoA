from flask import Blueprint, request, jsonify, render_template
import logging
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    logger.info("Página principal accedida")
    return render_template('index.html')

@main.route('/api/analyze', methods=['POST'])
def analyze_code():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        logger.info(f"Análisis solicitado - Longitud: {len(code)} caracteres")
        
        # Inicializar componentes
        from app.analyzers.symbol_table import SymbolTable
        from app.analyzers.lexical_analyzer import LexicalAnalyzer
        from app.analyzers.syntax_analyzer import SyntaxAnalyzer
        from app.models.analysis_result import AnalysisResult
        
        symbol_table = SymbolTable()
        symbol_table.initialize_keywords()
        
        # Análisis léxico
        lex_analyzer = LexicalAnalyzer(code, symbol_table)
        lexical_result = lex_analyzer.analyze()
        
        # Análisis sintáctico (si el léxico fue exitoso o tiene pocos errores)
        syntax_result = {'success': False, 'errors': ['No se realizó análisis sintáctico']}
        
        if lexical_result['success'] or len(lexical_result['errors']) == 0:
            try:
                syntax_analyzer = SyntaxAnalyzer(lex_analyzer, symbol_table)
                syntax_result = syntax_analyzer.analyze()
            except Exception as e:
                syntax_result = {
                    'success': False, 
                    'errors': [f'Error en análisis sintáctico: {str(e)}']
                }
        else:
            syntax_result = {'success': False, 'errors': ['Error léxico detectado']}
        
        # Preparar respuesta
        result = AnalysisResult(lexical_result, syntax_result, symbol_table)
        result_dict = result.to_dict()
        
        logger.info(f"Análisis completado - Éxito: {result_dict['overall_success']}")
        
        return jsonify(result_dict)
        
    except Exception as e:
        logger.error(f"Error en el servidor: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Error en el servidor: {str(e)}'
        }), 500

@main.route('/api/examples/<example_name>', methods=['GET'])
def get_example(example_name):
    try:
        examples = {
            'semaforo': 'app/examples/semaforo.emb',
            'temperatura': 'app/examples/temperatura.emb',
            'puerta': 'app/examples/puerta.emb'
        }
        
        if example_name in examples:
            file_path = examples[example_name]
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                logger.info(f"Ejemplo cargado: {example_name}")
                return jsonify({'success': True, 'code': content})
            else:
                return jsonify({'success': False, 'error': 'Archivo de ejemplo no encontrado'}), 404
        else:
            return jsonify({'success': False, 'error': 'Ejemplo no encontrado'}), 404
            
    except Exception as e:
        logger.error(f"Error cargando ejemplo: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@main.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de salud simplificado"""
    return jsonify({'status': 'healthy', 'mode': 'local'})