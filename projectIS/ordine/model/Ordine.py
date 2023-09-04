
class Ordine:
    def __init__(self, prodotti,data,cliente,indirizzo,data_consegna,completato):
        super(Ordine, self).__init__()
        self.prodotti=prodotti
        self.data=data
        self.cliente=cliente
        self.indirizzo=indirizzo
        self.data_consegna = data_consegna
        self.completato=completato


