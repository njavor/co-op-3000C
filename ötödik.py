#5. Igaz-e, hogy minden szám nagyobb, mint 10?

def öt(lista):
    igaz_e= True
    i=0
    while igaz_e and i<len(lista):

        if lista[i]<10:
            igaz_e=False

        i+=1

    print (igaz_e)