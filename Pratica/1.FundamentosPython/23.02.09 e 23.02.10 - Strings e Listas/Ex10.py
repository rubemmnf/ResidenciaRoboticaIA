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
for i in range (M) :
    matriz.append ([0]*N)

vetor = []
elemento = 0

for i in range(M):
    for j in range (N):
        elemento = int(input("Insira o elemento: "))
        matriz[i][j] = elemento

#Solução
for j in range(N):
    for i in range(M):
        if matriz[i][j] % 6 == 0:
            vetor.append(matriz[i][j])

#Saída
print("A matriz inserida foi: ")
for i in range(M):
    print(matriz[i])

print("O vetor com os múltiplos de 6 é: \n", vetor)