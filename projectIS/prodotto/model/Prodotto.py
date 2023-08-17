
class Prodotto:
    def __init__(self, nome,tipo,prezzo,peso,ingredienti):
        super(Prodotto, self).__init__()
        self.nome=nome
        self.tipo=tipo
        self.prezzo=prezzo
        self.peso=peso
        self.ingredienti=ingredienti