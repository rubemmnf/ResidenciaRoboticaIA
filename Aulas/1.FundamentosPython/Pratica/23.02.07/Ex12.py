i=0
qtd = 0
soma = 0.0

while (i>=0):
    i = float(input("Insira um número:"))
    
    if i>=0:
        soma = soma + i
        qtd = qtd + 1

if qtd == 0:
    media = i
else:
    media = soma/qtd

print(media)