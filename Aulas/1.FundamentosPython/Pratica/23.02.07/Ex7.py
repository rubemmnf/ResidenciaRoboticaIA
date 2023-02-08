#Variáveis
inicio = int(input("Insira o valor inicial:"))
fim = int(input("Insira o valor final:"))
soma = 0
i=0

if inicio > fim:
    inicio, fim = fim, inicio

#Solução com For
#for i in range(inicio+1,fim,1):
#    if i % 2 == 1:
#        soma = soma + i

#Solução com While
i = inicio + 1 
while (i<fim):
    if i % 2 == 1:
        soma = soma + i
    i+=1

#Saída
print("O resultado é ", soma, " para ",inicio, " e ", fim)