import networkx as nx
import matplotlib.pyplot as plt

def crear_automata():
    # Creamos un Grafo Dirigido (DiGraph)
    G = nx.DiGraph()

    # Lista de transiciones (Origen, Destino, Etiqueta)
    # Basado en el análisis de tu imagen
    transiciones = [
        # --- Inicio y Setup ---
        ('q0', 'q1', 'KW_SETUP'),
        ('q1', 'q2', 'DELIM_COLON'),
        
        # Bloque Declaracion en Setup
        ('q2', 'q3', 'KW_PIN/LIT_FLOAT'),
        ('q3', 'q4', 'VAR'),
        ('q4', 'q5', 'OP_ASSIGN'),
        ('q5', 'q6', 'LIT_PIN'),
        ('q6', 'q2', 'DELIM_SEMICOLON'),
        
        # Bloque PinMode en Setup
        ('q2', 'q12', 'FUNC_PINMODE'),
        ('q12', 'q13', 'DELIM_LPARENT'),
        ('q13', 'q14', 'VAR'),
        ('q14', 'q15', 'DELIM_COMMA'),
        ('q15', 'q16', 'KW_IN/OUT'),
        ('q16', 'q6', 'C_PARENTESIS'), # Conecta al q6 para cerrar con ;
        
        # Salida de Setup a Loop
        ('q2', 'q7', 'KW_END'),
        ('q7', 'q8', 'KW_LOOP'),
        ('q8', 'q9', 'DELIM_COLON'),
        
        # --- Loop Principal (q9) ---
        
        # Funciones Simples (Delay, On, Off)
        ('q9', 'q11', 'FUNC_ON/OFF/DLY'),
        ('q11', 'q18', 'DELIM_LPARENT'),
        ('q18', 'q19', 'VAR/LIT_PIN'),
        ('q19', 'q20', 'DELIM_RPARENT'),
        ('q20', 'q9', 'DELIM_SEMICOLON'),
        
        # Declaraciones y Matemáticas
        ('q9', 'q10', 'KW_INT/FLOAT'),
        ('q10', 'q17', 'VAR'),
        ('q17', 'q22', 'OP_ASSIGN'),
        
        # -- Lectura
        ('q22', 'q23', 'FUNC_READ'),
        
        # -- Multiplicacion
        ('q22', 'q24', 'VAR'),
        ('q24', 'q25', 'OP_MULTIPLY'),
        ('q25', 'q23', 'LIT_FLOAT'),
        
        # -- Cierre matématico
        ('q23', 'q9', 'DELIM_SEMICOLON'),
        
        # Estructuras de Control (For/If)
        ('q9', 'q26', 'KW_FOR/IF'),
        ('q26', 'q27', 'DELIM_LPARENT'),
        ('q27', 'q28', 'VAR'),
        ('q28', 'q29', 'OP'),
        ('q29', 'q30', 'VAR'),
        ('q30', 'q31', 'DELIM_RPARENT'),
        ('q31', 'q9', 'DELIM_SEMICOLON'),
        
        # Fin
        ('q9', 'q21', 'FIN')
    ]

    # Añadir las aristas al grafo
    for origen, destino, etiqueta in transiciones:
        G.add_edge(origen, destino, label=etiqueta)
        
    return G

def revisar_automata(G):
    print("--- REVISIÓN DEL AUTOMATA ---")
    print(f"Total de Estados (Nodos): {G.number_of_nodes()}")
    print(f"Total de Transiciones (Aristas): {G.number_of_edges()}")
    print("-" * 30)
    print("Nodos centrales (Grado > 2):")
    for nodo, grado in G.degree():
        if grado > 2:
            print(f"Estado {nodo}: {grado} conexiones")
    print("-" * 30)

def graficar_automata(G):
    plt.figure(figsize=(16, 10)) # Tamaño grande para que se vea bien
    
    # Algoritmo de distribución (Layout). 
    # 'kamada_kawai' suele desenredar bien los grafos complejos, 
    # si no te gusta, cambia por nx.spring_layout(G, k=2)
    pos = nx.kamada_kawai_layout(G) 
    
    # Dibujar Nodos
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='#ffff99', edgecolors='black')
    
    # Dibujar Etiquetas de Nodos (q0, q1...)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    
    # Dibujar Aristas (Flechas)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    
    # Dibujar Etiquetas de las Aristas (Tokens)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, label_pos=0.5)
    
    plt.title("Visualización del Autómata de Sintaxis")
    plt.axis('off') # Ocultar ejes X/Y
    plt.show()

# --- Ejecución ---
if __name__ == "__main__":
    grafo = crear_automata()
    revisar_automata(grafo)
    graficar_automata(grafo)