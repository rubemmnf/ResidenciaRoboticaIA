#Código para receber números maiores ou iguais a zero até receber um negativo e retornar quais \\
#têm dois dígitos significativos na ordem inversa que foram digitados

#Entrada

N = int(input("Insira um número: "))
conjuntoInicial = [N]
conjuntoFinal = []

while N >= 0:
    N = int(input("Insira um número: "))
    conjuntoInicial.append(N)

#Solução
for num in conjuntoInicial:
    if num >= 10:
        conjuntoFinal.append(num)

#Saída
print("Os números com dois dígitos significativos são: ")
for num in conjuntoFinal[::-1]:
    print(num)