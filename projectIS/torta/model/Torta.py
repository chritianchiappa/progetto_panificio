class Torta:
    def __init__(self, base,ingredienti,prezzo, peso,candeline,scritta,richieste):
        super(Torta, self).__init__()
        self.base = base
        self.prezzo = prezzo
        self.peso = peso
        self.ingredienti = ingredienti
        self.candeline=candeline
        self.scritta=scritta
        self.richieste=richieste