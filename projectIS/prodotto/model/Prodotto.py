
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
                         self.quantita)  # Assicurati di copiare tutti gli attributi necessari
        # Copia gli altri attributi specifici se presenti
        return copia