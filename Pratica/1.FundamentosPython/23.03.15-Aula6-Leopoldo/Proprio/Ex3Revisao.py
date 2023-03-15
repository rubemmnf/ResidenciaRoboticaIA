def sublista (L,S):
    for l in L:
        if l in S:
            teste = L[L.index(l):L.index(l)+len(S)]
            if teste == S:
                return True
            
print(sublista([1,1,1],[1]))