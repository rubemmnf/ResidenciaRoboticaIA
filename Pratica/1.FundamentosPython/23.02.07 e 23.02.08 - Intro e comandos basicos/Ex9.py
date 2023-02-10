#Variáveis
valorN = int(input("Insira o valor de N: "))
i = 0
numPosicao = 0
final = 0

while valorN < 1:
    print("Inválido. Insira um número válido")

#Solução com For
#for i in range(i,valorN,1):
#    numPosicao = i + (i//2)*4 - 1

#Solução com While
while (i<valorN):
    numPosicao = i + (i//2)*4 - 1
    print(numPosicao)
    i+=1

final = numPosicao
print(final)