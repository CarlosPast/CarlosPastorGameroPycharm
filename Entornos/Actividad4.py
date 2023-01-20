

def actividad4(clave):
    pregunta1 = input("¿Cual es la clave? ").upper()

    while pregunta1 != clave:
       pregunta1 = input("Otra vez, ¿Cual es la clave? ").upper()

    else:
        print("Enhorabuena acertaste")

actividad4("12345EDD")