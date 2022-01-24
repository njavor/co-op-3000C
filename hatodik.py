def hat(lista):
    persix = 0
    for elem in lista:
        if elem %9 == 0:
            persix +=1
    print(persix)