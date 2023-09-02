
class Prodotto:
    def __init__(self, nome,tipo,prezzo,ingredienti,quantita):
        super(Prodotto, self).__init__()
        self.nome=nome
        self.tipo=tipo
        self.prezzo=prezzo
        self.ingredienti=ingredienti
        self.quantita=quantita