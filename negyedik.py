#4. Mennyi a sorozatban található számok átlagának a négyzete?
def négy(lista):

    szám_összeg_átlag_eredmény=0

    for elem in lista:
        elem +=szám_összeg_átlag_eredmény

    szám_összeg_átlag_eredmény%=len(lista)    

    szám_összeg_átlag_eredmény*=szám_összeg_átlag_eredmény

    print (szám_összeg_átlag_eredmény)
    
