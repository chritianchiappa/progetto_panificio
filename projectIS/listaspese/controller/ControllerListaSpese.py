from listaspese.model.ListaSpese import ListaSpese

class ControllerListaSpese:
    def __init__(self):
        super(ControllerListaSpese, self).__init__()
        self.model = ListaSpese()

    def inserisci_spesa(self, spesa):
        self.model.inserisci_spesa(spesa)
    def get_lista_spese(self):
        return self.model.get_lista_spese()

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()