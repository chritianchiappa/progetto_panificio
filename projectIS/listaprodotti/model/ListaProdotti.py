import json
import os.path
import pickle

from prodotto.model.Prodotto import Prodotto

class ListaProdotti:

    def __init__(self):
        super(ListaProdotti, self).__init__()
        self.lista_prodotti = []
        self.refresh_data()

    def inserisci_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)
        self.save_data()

    def get_lista_prodotti(self):
        return self.lista_prodotti

    def get_lista_marche(self):
        for prodotto in self.lista_prodotti:
            if prodotto.marca in self.lista_marche:
                pass
            else:
                self.lista_marche.append(prodotto.marca)
        return self.lista_marche

    def get_dimensione_lista(self):
        return len(self.lista_prodotti)




    # Metodo: ricarica in lista i dati da file pickle, se esistente e non vuoto, o dal file json
    def refresh_data(self):
        if os.path.isfile('listaprodotti/data/lista_prodotti_salvata.pickle') and os.stat('listaprodotti/data/lista_prodotti_salvata.pickle').st_size!=0:
            with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'rb') as f:
                try:
                    self.lista_prodotti = pickle.load(f)
                except EOFError:
                    return
        else:
            with open('listaprodotti/data/lista_prodotti_salvata.json') as f:
                lista_prodotti_json = json.load(f)
                for prodotto_da_caricare in lista_prodotti_json:
                    self.lista_prodotti.append(
                        Prodotto(
                            prodotto_da_caricare['nome'],
                            prodotto_da_caricare['tipo'],
                            prodotto_da_caricare['prezzo'],
                            prodotto_da_caricare['peso'],
                            prodotto_da_caricare['ingredienti'],
                            prodotto_da_caricare['liked'],
                            prodotto_da_caricare['quantita']))

    # Metodo: salva il contenuto della lista su file pickle
    def save_data(self):
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)

    # Metodo: salvo il contenuto di una lista in particolare su file pickle
    def save_data_specialized(self, lista_prodotti):
        with open('listaprodotti/data/DatabaseProdotti.pickle', 'wb') as handle:
            pickle.dump(lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)