#Código para a leitura e consulta de uma tabela de pessoas

codPessoa = 42
tab = {}
i = 0
soma = 0.0

while (codPessoa >= 1):
    codPessoa = int(input ('Digite o código da pessoa que deseja inserir: '))

    if codPessoa >= 1:
        nomePessoa = str(input ('Digite o nome da pessoa que deseja inserir: '))

        salario = float(input ('Digite o salário da pessoa: '))
        while (salario <= 0) :
            codCentro = int(input ('Salário deve ser inteiro e positivo. Tente novamente: '))
        tab [codPessoa] = (nomePessoa, salario)


salarioMax = float(input("Insira o valor máximo de salário: "))
while salarioMax < 0:
    salarioMax = float(input("Inválido. Insira um valor máximo de salário válido: "))
    
tabAux = {}
for codigo in tab:
    if tab[codigo][1] <= salarioMax:
        tabAux[codigo] = tab[codigo][0]
        i += 1
        soma += tab[codigo][1]
        
if i > 0:
    print ("As pessoas com um salário inferior a esse são: \n", tabAux)
    print ("Ou seja ", i, " pessoas nessa faixa")
    print ("E a média deles é: ", soma/i)

else:
    print ("Nenhuma pessoa encontrada")

print ("Fim de Programa")