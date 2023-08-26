from listaprodotti.model.ListaProdotti import ListaProdotti

"""
    CONTROLLER DELLA LISTA DEI PRODOTTI
        Contiene le funzionalità principali del programma per quanto riguarda la gestione dei prodotti
"""


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



    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()

    def save_data_specialized(self, lista_prodotti):
        self.model.save_data_specialized(lista_prodotti)