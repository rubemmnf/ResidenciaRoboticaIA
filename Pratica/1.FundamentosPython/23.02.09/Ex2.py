#Código para ler o nome do usuário e escrever "em escala"

nomeUsuario = str(input("Insira seu nome: "))
compo = ""

for letra in nomeUsuario:
    compo = compo + letra
    print(compo)