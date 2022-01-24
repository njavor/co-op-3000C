"""
Olvassuk be az alábbi fájl tartalmmát egy listába/tömbbe,
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát!
1. Van-e a sorozatban 100-zal osztható szám?
2. Írjuk ki az utolsó 7-tel osztható szám indexét!
3. Írjuk ki az első 19-cel osztható szám indexét!
4. Mennyi a sorozatban található számok átlagának a négyzete?
5. Igaz-e, hogy minden szám nagyobb, mint 10?
6. Hány 9-cel osztható szám található a sorozatban?
7. Írjuk ki a sorozatban található 15-tel osztható számok felét!
8. Hány eleme van a sorozatnak?
9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?
10. Mennyi a sorozatban található legkisebb szám fele?
"""
from első import egy

lista = []
with open("input.txt","r",encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))

egy()