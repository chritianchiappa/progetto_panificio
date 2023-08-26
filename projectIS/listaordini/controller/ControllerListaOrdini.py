from listaordini.model.ListaOrdini import ListaOrdini


class ControllerListaOrdini:
    def __init__(self):
        super(ControllerListaOrdini, self).__init__()
        self.model = ListaOrdini()

    def get_lista_ordini(self):
        return self.model.get_lista_ordini()

    def get_lista_ordini_non_completati(self):
        return self.model.get_lista_ordini_non_completati()

    def inserisci_ordine(self, ordine):
        self.model.inserisci_ordine(ordine)


    def load_data(self):
        self.model.load_data()

    def save_data(self):
        self.model.save_data()