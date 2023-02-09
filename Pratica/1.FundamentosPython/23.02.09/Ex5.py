#Código para ler 2 vetores de tamanho N, juntá-los e imprimir os 3

N = int(input("Insira o valor de N: "))

while N <= 0:
    N = int(input("Inválido. Insira o valor de N: "))

vetor1 = str(input("Insira o primeiro valor: "))
vetor2 = str(input("Insira o segundo valor: "))

vetorSoma = vetor1 + vetor2

print(vetor1)
print(vetor2)
print(vetorSoma)