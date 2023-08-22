import os
import pickle
from datetime import datetime,timedelta
class ListaIngredienti():
    def __init__(self):
        self.lista_ingredienti = []
        if os.path.isfile('listaingredienti/data/lista_ingredienti_salvata.pickle'):
            with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'rb') as f:
                self.lista_ingredienti = pickle.load(f)

    def inserisci_ingrediente(self, ingrediente):
        self.lista_ingredienti.append(ingrediente)

    def get_ingrediente_by_index(self, index):
        return self.lista_ingrediente[index]

    def rimuovi_ingrediente_by_index(self,index):
        self.lista_ingredienti.pop(index)

    def check_ingrediente_by_id(self,id):
        for ingrediente in self.lista_ingredienti:
            if ingrediente.id==id:
                return ingrediente
        return None

    def rimuovi_ingrediente_by_id(self, id):
        def is_selected(ingrediente):
            if ingrediente.id == id:
                return True
            return False
        self.lista_ingredienti.remove(list(filter(is_selected, self.lista_ingredienti))[0])

    def get_lista_ingredienti(self):
        return self.lista_ingredienti

    def is_scaduto(self):
        oggi = datetime.now().date()
        return oggi > self.data_scadenza

    def save_data(self):
        with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)