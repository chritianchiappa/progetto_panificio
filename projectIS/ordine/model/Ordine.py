
class Ordine:
    def __init__(self, prodotti,data,cliente,completato):
        super(Ordine, self).__init__()
        self.prodotti=prodotti
        self.data=data
        self.cliente=cliente
        self.completato=completato