import os
import pickle
import json
from datetime import datetime,timedelta

from ingrediente.model.Ingrediente import Ingrediente


class ListaIngredienti():
    def __init__(self):
        self.lista_ingredienti = []
        self.refresh_data()

    def inserisci_ingrediente(self, ingrediente):
        self.lista_ingredienti.append(ingrediente)

    def get_ingrediente_by_index(self, index):
        return self.lista_ingredienti[index]

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
    def refresh_data(self):
        if os.path.isfile('listaingredienti/data/lista_ingredienti_salvata.pickle') and os.stat('listaingredienti/data/lista_ingredienti_salvata.pickle').st_size!=0:
            with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'rb') as f:
                try:
                    self.lista_ingredienti = pickle.load(f)
                except EOFError:
                    return
        else:
            with open('listaingredienti/data/lista_ingredienti_salvata.json') as f:
                lista_ingredienti_json = json.load(f)
                for ingrediente_da_caricare in lista_ingredienti_json:

                    self.lista_ingredienti.append(
                        Ingrediente(
                            ingrediente_da_caricare['nome'],
                            ingrediente_da_caricare['prezzo'],
                            ingrediente_da_caricare['quantita'],
                            ingrediente_da_caricare['allergeni'],
                            ingrediente_da_caricare['scadenza']))

    def save_data(self):
        with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)