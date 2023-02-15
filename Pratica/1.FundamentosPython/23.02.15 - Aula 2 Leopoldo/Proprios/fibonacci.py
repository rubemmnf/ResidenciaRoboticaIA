#Fibonacci function that returns all numbers in the Fibonacci sequence per line until that one
# def fibonacci (n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for i in range(10):
#     print(fibonacci(i))

# Função de fibonnaci que retorna não só o número da sequência, mas também todos os elementos anteriores da sequência pulando o primeiro 0
def fibonacci_iterativo(n):
    fib = [1, 1]
    if n == 0:
        return fib[0]
    else:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
print(fibonacci_iterativo(10))
print(type(fibonacci_iterativo(20)))

#Função para imprimir a lista em uma arquivo novo com o nome "fibonacci.txt" chamando a função anterior
#Imprimindo apenas um elemento por linha
def imprimir_fibonacci(n):
    with open("fibonacci.txt", "w") as arquivo:
        for i in range(n):
            termo = fibonacci_iterativo(n)[i]
            arquivo.write(str(termo) + "\n")

imprimir_fibonacci(10)    