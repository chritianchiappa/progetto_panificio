import os
import pickle
from crittografia.crittografa import CryptoManager
from utilizzatore.model.Dipendente import Dipendente
crypto_manager = CryptoManager()


class ListaDipendenti():
    def __init__(self):
        self.lista_dipendenti = []
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                dati_criptati=f.read()
                dati_decriptati=crypto_manager.decrittografa_dati(dati_criptati)
                self.lista_dipendenti = pickle.loads(dati_decriptati)

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

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
        dati_criptati = crypto_manager.cripta_dati(pickle.dumps(self.lista_dipendenti))
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            handle.write(dati_criptati)