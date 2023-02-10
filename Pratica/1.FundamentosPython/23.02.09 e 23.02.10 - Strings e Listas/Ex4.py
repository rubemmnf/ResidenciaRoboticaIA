#Código para ler o nome completo do usuário e escrever o primeiro e o último em maiúsculas

nomeCompleto = str(input("Insira seu nome completo: "))

nomeCompletoSeparado = nomeCompleto.split(" ")

nomeCompletoAlterado = nomeCompletoSeparado

nomeCompletoAlterado[0] = nomeCompletoAlterado[0].upper()
nomeCompletoAlterado[-1] = nomeCompletoAlterado[-1].upper()

nomeCompletoFinal = " ".join(nomeCompletoAlterado)

print(nomeCompletoFinal)