tab = []
n = idMax = idMin = qtd = 0

cpf = int(input("CPF: "))
while cpf <= 0:
    cpf = int(input("Digite um CPF válido: "))
while cpf > 0 and qtd < 200:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    while idade < 0:
        idade = int(input("Inválida. Idade: "))
    tab.append((cpf, nome, idade))
    qtd = qtd + 1
    cpf = int(input("CPF: "))

if cpf > 0:
    print('Leitura interrompida, último CPF desperezado')

n = int(input("Qtd de intervalos: "))
while n <=0:
    n = int(input("Inválido. Qtd de intervalos: "))

for i in range(n):
    idMin = int(input("Idade mínima: "))
    while idMin < 0:
        idMin = int(input("Inválida. Idade mínima: "))
    idMax = int(input("Idade máxima: "))
    if idMax >= idMin:
        qtd2 = 0
        for ch in range(len(tab)):
            if tab[ch][2] >= idMin and tab[ch][2] <= idMax:
                print(tab[ch][0], tab[ch][1], tab[ch][2])
                qtd2 = qtd2 + 1
        print("Qtd de alunos no intervalo = ", qtd2)
    else:
        print("Intervalo inválido, desprezado.")