#entrada
numero1 = int(input("Insira o primeiro inteiro:"))
numero2 = int(input("Insira o segundo inteiro:"))

while (numero2 == 0):
    numero2 = int(input("Inválido, digite novamente o segundo inteiro:"))

#potencial problema
if numero2 == 0:
    numero2 = int(input("Insira um número diferente de 0:"))

resto = numero1 % numero2

#resolução
if resto == 0:
    print("O resto é 0, o primeiro número é", numero1)
else:
    print("O resto não é 0, o quadrado do resto é:", resto*resto)