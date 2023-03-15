def contarPalavras(a):
    conteudo = open(a,"r")
    conta = 0
    for linha in conteudo:
        palavras = linha.strip().split(" ")
        conta += len(palavras)
    return conta