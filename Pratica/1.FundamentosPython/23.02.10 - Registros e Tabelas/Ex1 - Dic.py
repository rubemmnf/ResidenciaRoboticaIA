#Código para a leitura e consulta de uma tabela de cursos

codCurso = 2
tab = {}
i = 0

while (codCurso != 0):
    codCurso = int(input ('Digite o código do curso que deseja inserir: '))
    while (codCurso < 0) :
        codCurso = int(input ('Código deve ser inteiro e positivo. Tente novamente: '))

    if codCurso != 0:
        nomeCurso = str(input ('Digite o nome do curso que deseja inserir: '))

        codCentro = int(input ('Digite o código do centro que esse curso pertence: '))
        while (codCentro < 1) :
            codCentro = int(input ('Código deve ser inteiro e positivo. Tente novamente: '))
        tab [codCurso] = (nomeCurso, codCentro)

codBusca = int(input ('Digite um código de centro para busca (<=0 para parar): '))
while codBusca > 0 :
    tabAux = {}
    for codigo in tab:
        if tab[codigo][1] == codBusca:
            tabAux[codigo] = tab[codigo][0]
            i += 1
            
    if i > 0:
        print ("Os cursos desse centro são: \n", tabAux)
    else:
        print ("Nenhum curso encontrado")
    codBusca = int(input ('Digite outro código para busca (<=0 para parar): '))
    i = 0

print ("Fim de Programa")