
class Ordine:
    def __init__(self, prodotti,data,cliente,indirizzo,completato):
        super(Ordine, self).__init__()
        self.prodotti=prodotti
        self.data=data
        self.cliente=cliente
        self.indirizzo=indirizzo
        self.completato=completato

