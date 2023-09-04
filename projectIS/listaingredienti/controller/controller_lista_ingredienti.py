from listaingredienti.model.lista_ingredienti import ListaIngredienti



class ControllerListaIngredienti:
    def __init__(self):
        super(ControllerListaIngredienti, self).__init__()
        self.model = ListaIngredienti()

    def get_lista_ingredienti(self):
        return self.model.get_lista_ingredienti()

    def get_ingrediente_by_index(self,index):
        return self.model.get_ingrediente_by_index(index)
    def inserisci_ingrediente(self, ingrediente):
        self.model.inserisci_ingrediente(ingrediente)
    def rimuovi_ingrediente_by_index(self,index):
        self.model.rimuovi_ingrediente_by_index(index)

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()

    def save_data_specialized(self, lista_ingredienti):
        self.model.save_data_specialized(lista_ingredienti)