# 1. Van-e a sorozatban 100-zal osztható szám?

def egy(lista):
    van_e= False
    i = 0
    while not van_e and i<len(lista):
        
        if(lista[i]==100):
            van_e=True
        i+=1
    
    print(van_e)