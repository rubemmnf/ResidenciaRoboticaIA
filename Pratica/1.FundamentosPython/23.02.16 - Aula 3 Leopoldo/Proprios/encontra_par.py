#assumir que L é uma lista de inteiros e retornar o primeiro número par em L. 
# raise ValueError se não encontrar
def encontrar_numero_par(L):
    for num in L:
        if num % 2 == 0:
            return num
    raise ValueError ("Não encontrou número par")

print(encontrar_numero_par([1,2,3,4,5]))
print(encontrar_numero_par([1,3,4,5]))
print(encontrar_numero_par([1,3,5]))