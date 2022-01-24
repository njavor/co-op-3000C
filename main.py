from első import egy
from második import kettő
from harmadik import három
from negyedik import négy
from ötödik import öt
from hatodik import hat
from hetedik import hét
from nyolcadik import nyolc
from kilencedik import kilenc
from tizedik import tíz

lista = []
with open("input.txt","r",encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))

print("1. Van-e a sorozatban 100-zal osztható szám?")
egy(lista)
print("2. Írjuk ki az utolsó 7-tel osztható szám indexét!")
kettő(lista)
print("3. Írjuk ki az első 19-cel osztható szám indexét!")
három(lista)
print("4. Mennyi a sorozatban található számok átlagának a négyzete?")
négy(lista)
print("5. Igaz-e, hogy minden szám nagyobb, mint 10?")
öt(lista)
print("6. Hány 9-cel osztható szám található a sorozatban?")
hat(lista)
print("7. Írjuk ki a sorozatban található 15-tel osztható számok felét!")
hét(lista)
print("8. Hány eleme van a sorozatnak?")
nyolc(lista)
print("9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?")
kilenc(lista)
print("10. Mennyi a sorozatban található legkisebb szám fele?")
tíz(lista)