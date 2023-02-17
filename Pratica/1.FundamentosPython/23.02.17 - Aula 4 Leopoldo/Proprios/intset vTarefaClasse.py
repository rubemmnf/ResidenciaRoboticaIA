class Int_set(object):
    """Um Int_set é um conjunto de inteiros"""
      #Valor de um conjunto é representado por uma lista de inteiros, self._vals.
      #Cada inteiro em um set aparece em self._vals apenas uma vez.

    def __init__(self):
        """Cria conjunto vazio de inteiros"""
        self._vals = []

    def insert(self, e):
        """Assume que e tem um valor inteiro e insere e em self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assume que e tem um valor inteiro
           Retorna True se está em self, e False do contrário"""
        return e in self._vals

    def remove(self, e):
        """Assume que e tem um valor inteiro e remove e de self
           Lança ValueError se e não está em self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Retorna uma lista com os elementos de self._vals
           Nada pode ser assumido sobre a ordem dos elementos"""
        return self._vals[:]
    
    def union(self, other):
        """other é um objeto Int_set
           altera o estado de self de forma a conter exatamente 
           os elementos atuais mais os elementos de other."""
        for e in other.get_members():
            self.insert(e)

    def __str__(self):
        """Retorna uma representação em string de self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'

if __name__=='__main__':
    s = Int_set()
    s.insert(3)
    s.insert(4)
    t = Int_set()
    t.insert(4)
    t.insert(5)
    t.insert(6)
    print(str(s))
    print('O valor de s é', s)
    print('O valor de t é', t)
    s.union(t)
    print('O valor de s U t é', s)