def temElementosEmComum (L1, L2):
    for l in L1:
        if l in L2:
            return True

print(temElementosEmComum([1,2,3], [4,5,6]))