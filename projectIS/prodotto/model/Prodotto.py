
class Prodotto:
    def __init__(self, nome,tipo,prezzo,ingredienti,quantita):
        super(Prodotto, self).__init__()
        self.nome=nome
        self.tipo=tipo
        self.prezzo=prezzo
        self.ingredienti=ingredienti
        self.quantita=quantita

    def copia(self):
        # Crea una copia del prodotto
        copia = Prodotto(self.nome, self.tipo,self.prezzo, self.ingredienti,
                         self.quantita)

        return copia