#Código para ler 2 vetores de tamanho N, juntá-los e imprimir os 3

N = int(input("Insira o valor de N: "))

while N <= 0:
    N = int(input("Inválido. Insira o valor de N: "))

v1 = [0]*N
v2 = [0]*N
vRes = [0]*N

for i in range(N):
    v1[i] = int(input("Insira o elemento " + str(i+1) + 'º do primeiro vetor: '))
    
for i in range(N):
    v2[i] = int(input("Insira o elemento " + str(i+1) + 'º do segundo vetor: '))
    vRes[i] = v1[i] + v2[i]

print("V1 =",v1)
print("V2 =",v2)
print("Soma =",vRes)

#Não funcionaria inicializar os vetores todos na mesma linha pois seriam várias \\
# referências ao mesmo vetor