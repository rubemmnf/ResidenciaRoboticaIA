import sys 

arquivo = sys.argv[1]
maior = 0 

with open(arquivo, 'r') as f:
    for linha in f:
        num = int(linha.replace('\n',''))
        if num > maior:
            maior = num

print("o maior de todos os números no arquivo é: "+str(maior))