import os.path
import pickle

class ListaSpese:

    def __init__(self):
        super(ListaSpese, self).__init__()
        self.lista_spese = []
        self.refresh_data()

    def inserisci_spesa(self, spesa):
        self.lista_spese.append(spesa)
        self.save_data()
    def get_lista_spese(self):
        return self.lista_spese

    def refresh_data(self):
        if os.path.isfile('listaspese/data/lista_spese_salvata.pickle') and os.stat('listaspese/data/lista_spese_salvata.pickle').st_size!=0:
            with open('listaspese/data/lista_spese_salvata.pickle', 'rb') as f:
                try:
                    self.lista_spese = pickle.load(f)
                except EOFError:
                    return


    def save_data(self):
        with open('listaspese/data/lista_spese_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_spese, handle, pickle.HIGHEST_PROTOCOL)