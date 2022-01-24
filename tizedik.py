def tíz(lista):
    legkis = lista[0]
    for elem in lista:
        if legkis > elem:
            legkis = elem
    print(legkis/2)