def es_letra(c):
    codigo = ord(c)
    # 'A'-'Z' o 'a'-'z'
    if (codigo >= ord('A') and codigo <= ord('Z')) or (codigo >= ord('a') and codigo <= ord('z')):
        return True
    else:
        return False

def es_digito(c):
    codigo = ord(c)
    if codigo >= ord('0') and codigo <= ord('9'):
        return True
    else:
        return False

def afd_identificador(cadena):
    # estados: 0 = q0, 1 = q1, -1 = q_dead
    estado = 0
    i = 0

    while i < len(cadena):
        c = cadena[i]

        if estado == 0:
            # q0: debe venir una letra
            if es_letra(c):
                estado = 1
            else:
                estado = -1

        elif estado == 1:
            # q1: podemos leer letra o dígito y quedarnos en q1
            if es_letra(c) or es_digito(c):
                estado = 1
            else:
                estado = -1

        # estado muerto, ya no vale la pena seguir, pero igual avanzamos
        else:
            estado = -1

        i = i + 1

    # aceptación
    if estado == 1:
        return True
    else:
        return False