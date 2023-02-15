#Ler os números, separados por vírgulas, em linhas de um arquivo usando o with open e salvar 
#a soma de cada linha em uma lista
def ler_numeros_arquivo(arq):
    numsInit = []
    numsFinal = []
    with open(arq, 'r') as arquivo:
        for linha in arquivo:
            numsInit = map(int, linha.split(','))
            numsFinal.append(sum(numsInit))
    return numsFinal

#Ler uma lista e imprimir seus elementos em linhas em um arquivo usando o with open
def imprimir_numeros_arquivo(lista, arq):
    with open(arq, 'w') as arquivo:
        for num in lista:
            arquivo.write(str(num) + '\n')
    return

somas = ler_numeros_arquivo("valores.csv")
imprimir_numeros_arquivo (somas, "soma.txt")