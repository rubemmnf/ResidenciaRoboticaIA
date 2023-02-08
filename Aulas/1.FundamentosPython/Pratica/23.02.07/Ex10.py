#Variáveis
valorN = int(input("Insira o valor de N: "))
i = 0
j = 0

while valorN < 1:
    print("Inválido. Insira um número válido: ")

#Solução com For
'''for i in range(0, valorN, 1):
    num = int(input("Insira um número a ser convertido:"))
    roman = ""
    for j in range(num, 1, -1):
        if num // 1000 > 0:
            roman = roman + "M"
            num = num - 1000
        elif num // 900 > 0:
            roman = roman + "CM"
            num = num - 900
        elif num // 500 > 0:
            roman = roman + "D"
            num = num - 500
        elif num // 400 > 0:
            roman = roman + "CD"
            num = num - 400
        elif num // 100 > 0:
            roman = roman + "C"
            num = num - 100
        elif num // 90 > 0:
            roman = roman + "XC"
            num = num - 90
        elif num // 50 > 0:
            roman = roman + "L"
            num = num - 50
        elif num // 40 > 0:
            roman = roman + "XL"
            num = num - 40
        elif num // 10 > 0:
            roman = roman + "X"
            num = num - 10
        elif num // 9 > 0:
            roman = roman + "IX"
            num = num - 9
        elif num // 5 > 0:
            roman = roman + "V"
            num = num - 5
        elif num // 4 > 0:
            roman = roman + "IV"
            num = num - 4
        elif num // 1 > 0:
            roman = roman + "I"
            num = num - 1
    print(roman)'''

#Solução com While
while (i<valorN):
    num = int(input("Insira um número a ser convertido:"))
    roman = ""
    i += 1
    
    while (num>0):
        if num // 1000 > 0:
            roman = roman + "M"
            num = num - 1000
        elif num // 900 > 0:
            roman = roman + "CM"
            num = num - 900
        elif num // 500 > 0:
            roman = roman + "D"
            num = num - 500
        elif num // 400 > 0:
            roman = roman + "CD"
            num = num - 400
        elif num // 100 > 0:
            roman = roman + "C"
            num = num - 100
        elif num // 90 > 0:
            roman = roman + "XC"
            num = num - 90
        elif num // 50 > 0:
            roman = roman + "L"
            num = num - 50
        elif num // 40 > 0:
            roman = roman + "XL"
            num = num - 40
        elif num // 10 > 0:
            roman = roman + "X"
            num = num - 10
        elif num // 9 > 0:
            roman = roman + "IX"
            num = num - 9
        elif num // 5 > 0:
            roman = roman + "V"
            num = num - 5
        elif num // 4 > 0:
            roman = roman + "IV"
            num = num - 4
        elif num // 1 > 0:
            roman = roman + "I"
            num = num - 1
    print(roman)