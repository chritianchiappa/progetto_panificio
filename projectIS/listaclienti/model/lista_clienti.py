import os
import pickle
from crittografia.crittografa import CryptoManager

crypto_manager = CryptoManager()


class ListaClienti():
    def __init__(self):
        self.lista_clienti = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                dati_criptati=f.read()
                dati_decriptati=crypto_manager.decrittografa_dati(dati_criptati)
                self.lista_clienti = pickle.loads(dati_decriptati)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def rimuovi_cliente_by_id(self, id):
        def is_selected(cliente):
            if cliente.id == id:
                return True
            return False
        self.lista_clienti.remove(list(filter(is_selected, self.lista_clienti))[0])



    def ritorna_nome(self,cognome):
        for cliente in self.lista_clienti:
            if cliente.cognome==cognome:
                return cliente.nome
    def get_lista_clienti(self):
        return self.lista_clienti

    def save_data(self):
        dati_criptati = crypto_manager.cripta_dati(pickle.dumps(self.lista_clienti))
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            handle.write(dati_criptati)

