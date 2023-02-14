def ascendente(l):
    if len(l) <= 1:
        return True
    else:
        return l[0] < l[1] and ascendente(l[1:])

print (ascendente([1,2,3,4,5]))
print (ascendente([1,2,3,5,4]))
print (ascendente([12,17,52,88,176]))
print (ascendente([12,17,88,52,176]))