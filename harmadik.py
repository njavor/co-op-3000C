def három(lista):
    tizenkilenc_megvan=False
    i=0
    index=0
    while not tizenkilenc_megvan and i<len(lista):
        if lista[i]%19==0:
            index =i
            tizenkilenc_megvan=True

        i+=1

    print(index)    