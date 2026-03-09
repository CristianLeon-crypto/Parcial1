def es_pieza(c):
    # Piezas comunes en los ejemplos: p, k, b, q, r
    piezas = "pkbqr"
    if c.lower() in piezas:
        return True
    else:
        return False

def es_destino(c):
    # Casillas o piezas destino: letras o números
    if es_pieza(c) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
        return True
    else:
        return False

def afd_ajedrez(movimiento):
    estado = "S0"
    i = 0
    
    try:
        while i < len(movimiento):
            c = movimiento[i]
            
            if estado == "S0":
                if es_pieza(c):
                    estado = "S1"
                else:
                    estado = "S_ERROR"
            
            elif estado == "S1":
                if es_pieza(c):
                    estado = "S1" # Sigue leyendo piezas (ej: kbp)
                elif c == "-":
                    estado = "S2" # Inicio de ->
                elif c.upper() == "X":
                    estado = "S4" # Captura directa, saltamos a destino
                else:
                    estado = "S_ERROR"
            
            elif estado == "S2":
                if c == ">":
                    estado = "S4" # Completó ->, vamos a destino
                else:
                    estado = "S_ERROR"
            
            elif estado == "S4":
                if es_destino(c):
                    estado = "S4" # Leyendo el destino (ej: k4 o qn)
                else:
                    estado = "S_ERROR"
            
            if estado == "S_ERROR":
                break
                
            i = i + 1
            
        # El estado final de aceptación es S4 (destino leído)
        if estado == "S4":
            return True
        else:
            return False
            
    except Exception as e:
        print("Error en el proceso:", e)
        return False

# --- PRUEBAS ---
def ejecutar_pruebas():
    casos = ["p->k4", "kbpXqn", "r->h3", "abc->123", "p-k4"]
    
    print("### RESULTADOS PUNTO 1 (AJEDREZ) ###")
    for c in casos:
        res = afd_ajedrez(c)
        if res:
            print(f"Movimiento '{c}': VÁLIDO")
        else:
            print(f"Movimiento '{c}': INVÁLIDO")

ejecutar_pruebas()