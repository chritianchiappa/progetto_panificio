import os
import pickle

class ListaIngredienti():
    def __init__(self):
        self.lista_ingredienti = []
        if os.path.isfile('listaingredienti/data/lista_ingredienti_salvata.pickle'):
            with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'rb') as f:
                self.lista_ingredienti = pickle.load(f)

    def inserisci_ingrediente(self, ingrediente):
        self.lista_ingredienti.append(ingrediente)

    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    def rimuovi_dipendente_by_index(self,index):
        self.lista_dipendenti.pop(index)

    def check_dipendente_by_id(self,id):
        for dipendente in self.lista_dipendenti:
            if dipendente.id==id:
                return dipendente
        return None

    def rimuovi_dipendente_by_id(self, id):
        def is_selected(dipendente):
            if dipendente.id == id:
                return True
            return False
        self.lista_dipendenti.remove(list(filter(is_selected, self.lista_dipendenti))[0])

    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    def save_data(self):
        with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)