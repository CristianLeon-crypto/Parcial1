from AFDdeIDs import afd_identificador

def probar_afd_identificador():
    pruebas = [
        "x",        # ACEPTA
        "x1",       # ACEPTA
        "Abc123",   # ACEPTA
        "1abc",     # NO ACEPTA (empieza por dígito)
        "a-b"       # NO ACEPTA ('-' no está permitido)
    ]

    for s in pruebas:
        try:
            resultado = afd_identificador(s)
            if resultado:
                print("CADENA:", s, "-> ACEPTA")
            else:
                print("CADENA:", s, "-> NO ACEPTA")
        except Exception as e:
            # uso de try/except como pediste
            print("Error procesando cadena:", s, "Mensaje:", str(e))

probar_afd_identificador()