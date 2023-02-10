#Código para receber números maiores ou iguais a zero até receber um negativo e retornar quais \\
#têm dois dígitos significativos na ordem inversa que foram digitados para no máximo 1000 números

#Entrada

N = int(input("Insira um número: "))
conjuntoInicial = [N]
conjuntoFinal = []
i = 1

while N >= 0 and i < 1000:
    N = int(input("Insira um número: "))
    conjuntoInicial.append(N)
    i += 1

#Solução
for num in conjuntoInicial:
    if num >= 10:
        conjuntoFinal.append(num)

#Saída
print("Os números com dois dígitos significativos são: ")
for num in conjuntoFinal[::-1]:
    print(num)