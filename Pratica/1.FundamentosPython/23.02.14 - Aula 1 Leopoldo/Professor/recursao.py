def palindromo(s):
    def to_chars(s):
        s = s.lower()
        return s
    def is_palindromo(s):
        if len(s)<=1:
            return True
        else:
            return s[0] == s[-1] and is_palindromo(s[1:-1])
    return is_palindromo(to_chars(s))


# print(palindromo(""))
# print(palindromo("leol"))
# print(palindromo("Anna"))


def ascendente(lista):
    print("Executando ascendente("+str(lista)+")")
    if len(lista)<=1:
        print("  Retornando caso base: "+str(lista))
        return True
    else:
        print("  "+str(lista[0]) + "<=" + str(lista[1]) + " and ascendente("+str(lista[1:])+")")
        return lista[0]<=lista[1] and ascendente(lista[1:])

# ascendente([1,2,3,4,5])
# ascendente([2,3,1,4,5])

def busca_binaria(lista, low, high, elemento):
    if high>=low:
        meio = (high+low)//2
        # se for o elemento que estamos procurando, retorne a posição dele
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            return busca_binaria(lista, low, meio-1, elemento)
        elif lista[meio] < elemento:
            return busca_binaria(lista, meio+1, high, elemento)
    else: 
        return -1

l = [2,5,8,90,120]
x = 150
if ascendente(l):
    posicao = busca_binaria(l, 0, len(l)-1, x)
    print("----")
    if posicao == -1:
        print("Elemento não existe na lista")
    else:
        print("Elemento presente na posição "+str(posicao))