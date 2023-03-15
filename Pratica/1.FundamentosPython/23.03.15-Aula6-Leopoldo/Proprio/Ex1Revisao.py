def removerDuplicados (L):
    filtro = set()
    for elem in L:
        filtro.add(elem)
    
    listaFin = []
    for termo in filtro:
        listaFin.append(termo)
    return listaFin

print(removerDuplicados([1,1,2,3,1,2,3]))
