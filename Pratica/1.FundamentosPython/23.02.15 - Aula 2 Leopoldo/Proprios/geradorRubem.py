#Ler os números nas 3 primeiras linhas de um arquivo texto nums.txt usando o with open
#removendo os pulos de linha também
def ler_numeros_arquivo(arq):
    nums = []
    with open(arq, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            nums.append(int(linha))
    return nums
    
print("O maior número no arquivo é: ", max(ler_numeros_arquivo("nums.txt")))