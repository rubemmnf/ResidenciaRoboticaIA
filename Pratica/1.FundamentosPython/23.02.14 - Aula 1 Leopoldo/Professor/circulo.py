pi = 3.14159
def area(raio):
    return pi*(raio**2)
def circunferencia(raio):
    return 2*pi*raio
def superficie_esfera(raio):
    return 4.0*area(raio)
def volume_esfera(raio):
    return(4.0/3.0)*pi*(raio**3)

if __name__=='__main__':
    print(area(3))