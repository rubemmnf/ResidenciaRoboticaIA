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

def serie (n, nu1 = 37, nu2 = 38, de = 1):
    res = nu1 * nu2 / de
    if n > 1:
        nu1 = nu1 - (n-1)
        nu2 = nu2 - (n-1)
        de = de + (n-1)
        res = nu1 * nu2 / de + serie(n-1)
    return res

print(serie(N))