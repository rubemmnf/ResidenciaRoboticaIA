#Código para receber uma quantidade N de notas de alunos, calcular sua média e informar \\
# quais notas estão acima da média

#Entrada

N = int(input("Informe a quantidade N de alunos: "))
notas = []
soma = 0.0
media = 0.0
acimaMedia = []

while N <= 0:
    N = int(input("Inválido. Insira o valor de N: "))

for nota in range(N):
    nota = float(input("Insira a nota: "))
    notas.append(nota)

#Solução
for nota in notas:
    soma += nota

media = soma/N

for nota in notas:
    if nota > media:
        acimaMedia.append(nota)

#Saída
print("As notas acima da média são: ")
for nota in acimaMedia:
    print(nota)