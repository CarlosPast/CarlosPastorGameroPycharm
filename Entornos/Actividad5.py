


def actividad5():
    frase = input("Introduce una frase: ").lower()
    letra = input("Introduce una letra: ").lower()
    contador = 0


    for i in frase:
        if i == letra:
            contador += 1

    print("La letra " + letra + " aparece " + str(contador) + " veces en la frase: " + frase)


actividad5()