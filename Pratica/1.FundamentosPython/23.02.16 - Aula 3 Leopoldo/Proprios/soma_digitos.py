#Função que pega uma string e pega apenas os digitos numéricos nela e soma, usando apenas for, try
# except e int
def soma_digitos (s):
    aux = []
    i = 0
    j = 0
    for algarismo in s:
        try:
           aux.append(int(algarismo))
           i += 1
        except ValueError:
            pass
            j += 1
    print(s)
    print("números: ", i)
    print("letras: ", j)
    print("soma: ", sum(aux))

print (soma_digitos('123'))
print (soma_digitos('abc'))
print (soma_digitos('a1b2c'))

#Poderia fazer com uma variável soma já que não vai imprimir aux