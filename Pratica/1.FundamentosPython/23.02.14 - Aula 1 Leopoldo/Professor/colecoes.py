import collections
L = [1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,5,4,3,7,3,2,52,2,1]
cont = 0
for e in L:
    if e==52:
        cont+=1
print(cont)

counter = collections.Counter(L)
print(counter)