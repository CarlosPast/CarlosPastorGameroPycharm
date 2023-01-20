

def count_words(text):
    texto = text.split(" ")
    words = {}
    lista_numero = []
    for i in texto:
        cifra = texto.count(i)
        lista_numero.append(cifra)
    for ind in texto:
        if texto.count(ind) > 1:
            indice = texto.index(ind)
            lista_numero.remove(lista_numero[indice])
            texto.remove(ind)
    for i in range(len(lista_numero)):
        words[texto[i]]= lista_numero[i]
    print(words)
    return words


count_words("Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera")


