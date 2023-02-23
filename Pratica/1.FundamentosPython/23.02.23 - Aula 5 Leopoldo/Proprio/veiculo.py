#Classe Veículo com atributos de identificação, marca, modelo, velocidade máxima, quilometragem e capacidade opcional (com um valor padrão de 5)

class Veiculo:
    def __init__(self,  marca, modelo, velocidade_maxima, quilometragem, capacidade=5):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.quilometragem = quilometragem
        self.capacidade = capacidade

    def __str__(self):
        texto = f"Veículo {self.marca}, modelo {self.modelo}, atinge velocidade máxima {self.velocidade_maxima}km/h, comporta {self.capacidade} passageiros e já rodou {self.quilometragem}km"
        return texto

v = Veiculo("Fiat", "500", "150", "50000")
print(v)