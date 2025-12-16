graph [
  directed 1
  label "Automata Sintaxis Arduino"

  # --- Definicion de Nodos ---
  node [ id 0 label "q0" ]
  node [ id 1 label "q1" ]
  node [ id 2 label "q2" ]
  node [ id 3 label "q3" ]
  node [ id 4 label "q4" ]
  node [ id 5 label "q5" ]
  node [ id 6 label "q6" ]
  node [ id 7 label "q7" ]
  node [ id 8 label "q8" ]
  node [ id 9 label "q9" ]
  node [ id 10 label "q10" ]
  node [ id 11 label "q11" ]
  node [ id 12 label "q12" ]
  node [ id 13 label "q13" ]
  node [ id 14 label "q14" ]
  node [ id 15 label "q15" ]
  node [ id 16 label "q16" ]
  node [ id 17 label "q17" ]
  node [ id 18 label "q18" ]
  node [ id 19 label "q19" ]
  node [ id 20 label "q20" ]
  node [ id 21 label "q21" ]
  node [ id 22 label "q22" ]
  node [ id 23 label "q23" ]
  node [ id 24 label "q24" ]
  node [ id 25 label "q25" ]
  node [ id 26 label "q26" ]
  node [ id 27 label "q27" ]
  node [ id 28 label "q28" ]
  node [ id 29 label "q29" ]
  node [ id 30 label "q30" ]
  node [ id 31 label "q31" ]

  # --- Definicion de Aristas (Transiciones) ---

  # Inicio -> Setup
  edge [ source 0 target 1 label "KW_SETUP" ]
  edge [ source 1 target 2 label "DELIM_COLON" ]

  # Bloque Setup (q2) - Declaracion
  edge [ source 2 target 3 label "KW_PIN, LIT_FLOAT" ]
  edge [ source 3 target 4 label "VAR" ]
  edge [ source 4 target 5 label "OP_ASSIGN" ]
  edge [ source 5 target 6 label "LIT_PIN" ]
  edge [ source 6 target 2 label "DELIM_SEMICOLON" ]

  # Bloque Setup (q2) - PinMode
  edge [ source 2 target 12 label "FUNC_PINMODE" ]
  edge [ source 12 target 13 label "DELIM_LPARENT" ]
  edge [ source 13 target 14 label "VAR" ]
  edge [ source 14 target 15 label "DELIM_COMMA" ]
  edge [ source 15 target 16 label "KW_OUTPUT" ]
  edge [ source 15 target 16 label "KW_INPUT" ]
  edge [ source 16 target 6 label "C_PARENTESIS" ]

  # Salida de Setup -> Loop
  edge [ source 2 target 7 label "KW_END" ]
  edge [ source 7 target 8 label "KW_LOOP" ]
  edge [ source 8 target 9 label "DELIM_COLON" ]

  # Loop Principal (q9) - Funciones (On/Off/Delay)
  edge [ source 9 target 11 label "FUNCS_OFF" ]
  edge [ source 9 target 11 label "FUNC_ON" ]
  edge [ source 9 target 11 label "FUNC_DELAY" ]
  edge [ source 11 target 18 label "DELIM_LPARENT" ]
  edge [ source 18 target 19 label "VAR" ]
  edge [ source 18 target 19 label "LIT_PIN" ]
  edge [ source 19 target 20 label "DELIM_RPARENT" ]
  edge [ source 20 target 9 label "DELIM_SEMICOLON" ]

  # Loop Principal (q9) - Declaracion y Operaciones
  edge [ source 9 target 10 label "KW_FLOAT" ]
  edge [ source 9 target 10 label "KW_INT" ]
  edge [ source 10 target 17 label "VAR" ]
  edge [ source 17 target 22 label "OP_ASSIGN" ]
  
  # Operacion Lectura
  edge [ source 22 target 23 label "FUNC_READ" ]
  
  # Operacion Multiplicacion
  edge [ source 22 target 24 label "VAR" ]
  edge [ source 24 target 25 label "OP_MULTIPLY" ]
  edge [ source 25 target 23 label "LIT_FLOAT" ]
  
  # Cierre de instruccion matematica
  edge [ source 23 target 9 label "DELIM_SEMICOLON" ]

  # Loop Principal (q9) - Estructuras de Control (For/If)
  edge [ source 9 target 26 label "KW_FOR" ]
  edge [ source 9 target 26 label "KW_IF" ]
  edge [ source 26 target 27 label "DELIM_LPARENT" ]
  edge [ source 27 target 28 label "VAR" ]
  edge [ source 28 target 29 label "OP" ]
  edge [ source 29 target 30 label "VAR" ]
  edge [ source 30 target 31 label "DELIM_RPARENT" ]
  edge [ source 31 target 9 label "DELIM_SEMICOLON" ]

  # Fin de Programa
  edge [ source 9 target 21 label "FIN" ]
]