from listaingredienti.model.lista_ingredienti import ListaIngredienti



class ControllerListaIngredienti:
    def __init__(self):
        super(ControllerListaIngredienti, self).__init__()
        self.model = ListaIngredienti()

    def get_lista_ingredienti(self):
        return self.model.get_lista_prodotti()


    def inserisci_ingrediente(self, ingrediente):
        self.model.inserisci_ingrediente(ingrediente)

    def get_ingrediente_by_code(self, code):
        return self.model.get_prodotto_by_code(code)

    def get_nome_prodotto_by_code(self, codice):
        return self.model.get_nome_prodotto_by_code(codice)

    def elimina_prodotto_by_codice(self, codice_prodotto, lista_prodotti):
        self.model.elimina_prodotto(codice_prodotto, lista_prodotti)

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()

    def save_data_specialized(self, lista_prodotti):
        self.model.save_data_specialized(lista_prodotti)