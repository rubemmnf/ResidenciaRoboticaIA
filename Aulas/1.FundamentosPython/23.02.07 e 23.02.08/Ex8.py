#Variáveis
inicio = int(input("Insira o valor inicial:"))
fim = int(input("Insira o valor final:"))
i=0

#Solução com For
for i in range(inicio,fim+1,1):
    print(i, "ºF\t", (i-32)*5/9, "ºC")

#Solução com While
#i = inicio 
#while (i<=fim):
#    print(i, "ºF\t", (i-32)*5/9, "ºC")
#    i+=1