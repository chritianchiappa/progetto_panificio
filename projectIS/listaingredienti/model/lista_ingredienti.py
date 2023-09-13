import os
import pickle
import json
from datetime import datetime,timedelta

from ingrediente.model.Ingrediente import Ingrediente


class ListaIngredienti():
    def __init__(self):
        super(ListaIngredienti, self).__init__()
        self.lista_ingredienti = []
        self.refresh_data()

    def inserisci_ingrediente(self, ingrediente):
        self.lista_ingredienti.append(ingrediente)

    def get_ingrediente_by_index(self, index):
        return self.lista_ingredienti[index]

    def rimuovi_ingrediente_by_index(self,index):
        self.lista_ingredienti.pop(index)




    def get_lista_ingredienti(self):
        return self.lista_ingredienti


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
                    scadenza_str = ingrediente_da_caricare['scadenza']
                    scadenza_date = datetime.strptime(scadenza_str, "%d-%m-%Y").date()
                    self.lista_ingredienti.append(
                        Ingrediente(
                            ingrediente_da_caricare['nome'],
                            ingrediente_da_caricare['prezzo'],
                            ingrediente_da_caricare['unita_misura'],
                            ingrediente_da_caricare['quantita'],
                            ingrediente_da_caricare['allergeni'],
                            scadenza_date))

    def save_data(self):
        with open('listaingredienti/data/lista_ingredienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)