def desmembrar (numero):
    lista = []
    numero = str(numero)
    for letra in numero:
        lista.append(int(letra))
    return lista

def inverter (num):
    return desmembrar(num)[::-1]

inicio = 100
fim = 5000


for i in range(inicio, fim):
    cont = 0
    for j in range(len(desmembrar(i))):
        if desmembrar(i)[j] == inverter(i)[j]:
            cont += 1
    if cont == len(desmembrar(i)):
        print(i)
