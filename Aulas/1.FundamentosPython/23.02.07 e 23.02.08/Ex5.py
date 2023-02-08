#Variáveis
numero = int(input("Insira um número inteiro:"))
fatorial = 0
i = numero

while numero < 1:
    print("Inválido. Insira um número válido")

#Solução com for
#for i in range(numero,0,-1):
#    fatorial = fatorial + i

#print(fatorial)

#Solução com while
while (i>0):
    fatorial = fatorial + i
    i-=1

print(fatorial)