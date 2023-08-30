import os.path
import pickle

class ListaOrdini:

    def __init__(self):
        self.lista_ordini = []
        self.load_data()

    def inserisci_ordine(self, ordine):
        self.lista_ordini.append(ordine)

    def get_lista_ordini(self):
        return self.lista_ordini
    def get_lista_ordini_non_completati(self):
        lista_ordini_non_completati=[]
        for ordine in self.get_lista_ordini():
            if ordine.completato==False:
                lista_ordini_non_completati.append(ordine)
        return lista_ordini_non_completati



    def load_data(self):
        if os.path.isfile('listaordini/data/lista_ordini_salvata.pickle') and os.stat('listaordini/data/lista_ordini_salvata.pickle').st_size!=0:
            with open('listaordini/data/lista_ordini_salvata.pickle', 'rb') as f:
                try:
                    self.lista_ordini = pickle.load(f)
                except EOFError:
                    return

    # Metodo: salva il contenuto della lista su file pickle
    def save_data(self):
        with open('listaordini/data/lista_ordini_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)