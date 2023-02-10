#Código para ler 2 vetores de tamanho N, juntá-los e imprimir os 3

N = int(input("Insira o valor de N: "))

while N <= 0:
    N = int(input("Inválido. Insira o valor de N: "))

v1 = [0]*N
par = [0]*N
impar = [0]*N
qp = qi = 0

for i in range(N):
    v1[i] = int(input("Insira o elemento " + str(i+1) + 'º do primeiro vetor: '))
    if v1[i] % 2 == 0:
        par[qp] = v1[i]
        qp += 1
    else:
        impar[qi] = v1[i]
        qi += 1

par = par[:qp]
impar = impar[:qi]

print("Vetor inicial =",v1)
print("Pares =",par)
print("Ímpares =",impar)

#Não funcionaria inicializar os vetores todos na mesma linha pois seriam várias \\
# referências ao mesmo vetor