i=1
menor = 1

while (i!=0):
    i = int(input("Insira um número:"))
    if i==0:
        print("O menor número digitado foi ",menor)
    elif menor>i:
        menor = i