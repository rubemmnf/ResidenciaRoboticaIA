#Variáveis
limiteInf = 50
limiteSup = 100
i=50
soma = 0

#Solução com for
    #for i in range(limiteInf, limiteSup+1,2):
    #    soma = soma + i

    #print(soma)

#Solução com while
while (i <= limiteSup):
    soma = soma + i
    print(i)
    i = i + 2

print(soma)