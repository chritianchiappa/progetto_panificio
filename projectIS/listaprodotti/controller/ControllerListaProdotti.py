from listaprodotti.model.ListaProdotti import ListaProdotti


class ControllerListaProdotti:
    def __init__(self):
        super(ControllerListaProdotti, self).__init__()
        self.model = ListaProdotti()

    def get_lista_prodotti(self):
        return self.model.get_lista_prodotti()

    def get_prodotto_by_index(self,index):
        return self.model.get_prodotto_by_index(index)

    def inserisci_prodotto(self, prodotto):
        self.model.inserisci_prodotto(prodotto)

    def rimuovi_prodotto_by_index(self,index):
        self.model.rimuovi_prodotto_by_index(index)

    def aggiorna_quantita_prodotto(self,nome,quantita):
        self.model.aggiorna_quantita_prodotto(nome,quantita)

    def check_prodotto(self,nome):
        return self.model.check_prodotto(nome)

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()

    def save_data_specialized(self, lista_prodotti):
        self.model.save_data_specialized(lista_prodotti)