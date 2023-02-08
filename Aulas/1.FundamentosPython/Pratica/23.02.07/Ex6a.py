#Variáveis
S = 1
N = int(input("Insira N:"))
i = 1

while N < 1:
    print("Inválido. Insira um número válido")

#Solução com for
for i in range(1,N,1):
    aSomar = (i+2)/(i+1) 
    S = S + aSomar


#print(fatorial)

#Solução com while
#while (i<N):
#    aSomar = (i+2)/(i+1) 
#    S = S + aSomar
#    i+=1

print(S)