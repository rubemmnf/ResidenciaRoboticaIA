#Código para receber uma matriz M x N no máximo 4x8 com ambos definidos pelo usuário, passar por \\
# suas colunas salvando em uma lista os múltiplos de 6 e imprimir a lista e a matriz

#Entrada

M = int(input("Insira o número M (máx 4): "))
while M > 4 or M < 1:
    M = int(input("Inválido. Insira o número M (máx 4): "))

N = int(input("Insira o número N (máx 8): "))
while N > 8 or N < 1:
    N = int(input("Inválido. Insira o número N (máx 8): "))

matriz = []
vetor = []
elemento = 0

for j in range(M):
    for i in range (N):
        elemento = int(input("Insira o elemento: "))
#com erro        matriz[i][j] = elemento

#Solução
for j in range(N):
    for i in range(M):
        if matriz[i][j] % 6 == 0:
            print("corrigir")
##deve estar com erro também            vetor.append(matriz[i][j])

#Saída
print("A matriz inserida foi: ")
for i in range(N):
    print(matriz[i])

print("O vetor com os múltiplos de 6 é: \n", vetor)