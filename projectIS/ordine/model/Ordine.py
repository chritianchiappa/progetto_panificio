
class Ordine:
    def __init__(self, prodotti,data,importo,cliente,completato):
        super(Ordine, self).__init__()
        self.prodotti=prodotti
        self.data=data
        self.importo=importo
        self.cliente=cliente
        self.completato=completato