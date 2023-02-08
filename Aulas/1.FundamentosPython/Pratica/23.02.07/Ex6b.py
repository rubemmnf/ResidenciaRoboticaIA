#Variáveis
S = 0.0
N = int(input("Insira N:"))
i = 1

while N < 1 or N > 50:
    print("Inválido. Insira um número válido")

#Solução com for
#for i in range(1,N+1,1):
#    if i % 2 == 1:
#        aSomar = 2/(500 - (i-1)*10)
#    else:
#        aSomar = -5/(500 - (i-1)*10)
#    S = S + aSomar


#print(fatorial)

#Solução com while
while (i<=N):
    if i % 2 == 1:
        aSomar = 2/(500 - (i-1)*10)
    else:
        aSomar = -5/(500 - (i-1)*10) 
    S = S + aSomar
    i+=1

print(S)

#Como só alterna entre 2 e -5 poderia ser feito checando qual o valor atual
# e se for um mudar para o outro da forma

nume = 2
if nume == 2:
    nume = -5
else:
    nume = 2