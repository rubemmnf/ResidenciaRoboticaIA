def desmembrar (numero):
    lista = []
    numero = str(numero)
    for letra in numero:
        lista.append(int(letra))
    return lista

def conta_digitos (numeroGrande, algarismo):
    if numeroGrande < 0 or numeroGrande > 99999:
        print("Número inválido")
        return

    if algarismo < 0 or algarismo > 9:
        print("Algarismo inválido")
        return

    lista = desmembrar(str(int(numeroGrande)))
    cont = 0

    for num in lista:
        if num == algarismo:
            cont += 1

    return cont

num = int(input("Insira um inteiro positivo de até 5 dígitos: "))

while num > 99999:
    num = int(input("Inválido. Insira um inteiro positivo de até 5 dígitos: "))

while num > 0:
    print(f"O número {num:d} possui {conta_digitos(num, 9):d} ocorrência(s) do digito 9 nele")
    num = int(input("Insira um inteiro positivo de até 5 dígitos: "))