arq = open('nome.txt','w')
# teste = open('nome.txt', 'w')
print(arq.closed)
for i in range(2):
    nome = input('Digite um nome: ')
    arq.write(nome+'\n')
    # teste.write(nome+'\n')
arq.close()
# teste.close()
print(arq.closed)

def escrita():
    with open('nome.txt','w') as arq:
        for i in range(3):
            nome = input('Digite um nome: ')
            arq.write(nome+'\n')

def leitura(): 
    with open('nome.txt', 'r') as arquivo:
        # print(type(arquivo.read()))
        # print(arquivo.read())
        for linha in arquivo: 
            print(linha[:-1])

def escrita_leitura():
    with open('nome.txt','a') as arq:
        for i in range(3):
            nome = input('Digite um nome: ')
            arq.write(nome+'\n')


# escrita_leitura()
# leitura()