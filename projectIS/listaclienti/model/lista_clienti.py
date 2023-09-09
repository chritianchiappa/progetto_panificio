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

    def aggiorna_carrello_cliente(self, email,password, nuovo_carrello):
        cliente_t=self.check_cliente(email,password)
        cliente_t.carrello=nuovo_carrello
        self.save_data()
    def aggiorna_whishlist_cliente(self,email,password,nuova_whishlist):
        cliente_t=self.check_cliente(email,password)
        cliente_t.whishlist=nuova_whishlist
        self.save_data()

    def rimuovi_cliente_by_id(self, id):
        def is_selected(cliente):
            if cliente.id == id:
                return True
            return False
        self.lista_clienti.remove(list(filter(is_selected, self.lista_clienti))[0])


    def check_cliente(self,email,password):
        for cliente in self.lista_clienti:
            if cliente.email == email and cliente.password == password:
                return cliente
        return None
    def check_email(self,email):
        for cliente in self.lista_clienti:
            if cliente.email == email:
                return True
        return False
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

