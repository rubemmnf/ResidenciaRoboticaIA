#Versão anterior

#Variáveis
S = 0
N = int(input("Insira N:"))
i = 1

while N < 1:
    print("Inválido. Insira um número válido")

#Solução com for
for i in range(i,N+1,1):
    aSomar = (38 - i) * (39 - i) / i
    S = S + aSomar

#print(fatorial)

#Solução com while
#while (i<=N):
#    aSomar = (38 - i) * (39 - i) / i
#    S = S + aSomar
#    i+=1"

print(S)

#Versão com recursividade