def kilenc(lista):
    van = False
    i = 0
    while i<len(lista)-1 and not van:
        if lista[i] < 0 and lista[i+1] > 0:
            van = True
    print(van)