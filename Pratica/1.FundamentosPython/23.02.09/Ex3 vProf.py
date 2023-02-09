#Código para contar a quantidade de vezes que o primeiro texto aparece no segundo

proc = str(input("Insira a primeira palavra: "))
texto = str(input("Insira a segunda palavra: "))
cont = 0

pos = texto.find(proc)

while pos != -1:
    cont = cont + 1
    pos = texto.find(proc, pos +1)

#conta certo "ana" em "banana"
print("A primeira aparece ", cont, " vezes na segunda.")

#conta errado "ana" em "banana"
print("A primeira aparece ", texto.count(proc), " vezes na segunda.")

#Testar com "aa" e "aaaaaaa" para visualizar a diferença