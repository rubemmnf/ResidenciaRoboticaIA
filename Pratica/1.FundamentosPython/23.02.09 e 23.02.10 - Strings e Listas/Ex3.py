#Código para contar a quantidade de vezes que o primeiro texto aparece no segundo

palavra1 = str(input("Insira a primeira palavra: "))
palavra2 = str(input("Insira a segunda palavra: "))

print("A primeira aparece ", palavra2.count(palavra1), " vezes na segunda.")

#não conta certo "ana" em "banana"