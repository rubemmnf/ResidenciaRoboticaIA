num = int(input("Insira um número inteiro positivo:"))
cont = 0

if num == 1:
    print("Não é primo")
else:
    while (num <= 0):
        num = int(input("Inválido. Insira um número inteiro positivo:"))

    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    
    if cont == 2:
        print("É primo")
    else:
        print("Não é primo")

#Feito com while diminui o uso de memória por já sair do loop quando não for primo