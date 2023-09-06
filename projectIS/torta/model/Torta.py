class Torta:
    def __init__(self, base,farciture,copertura,richieste,prezzo, peso):
        super(Torta, self).__init__()
        self.base = base
        self.farciture = farciture
        self.copertura = copertura
        self.prezzo = prezzo
        self.peso = peso
        self.richieste=richieste