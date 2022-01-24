lista = []
with open(".txt","r",encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))