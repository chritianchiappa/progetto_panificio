from prodotto.controller.ControllerProdotto import ControllerProdotto
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
class ControllerCliente():
    def __init__(self, cliente):
        self.model = cliente
        self.controller_lista_clienti= ControllerListaClienti()

    def get_nome_cliente(self):
        return str(self.model.nome)

    def get_cognome_cliente(self):
        return str(self.model.cognome)

    def get_carrello_cliente(self):
        return self.model.carrello

    def aggiungi_prodotto_carrello(self,prodotto):
        self.model.carrello.append(prodotto)
        self.controller_lista_clienti.aggiorna_carrello_cliente(self.model, self.model.carrello)

    def get_whishlist_cliente(self):
        return self.model.whishlist

    def get_telefono_cliente(self):
        return self.model.telefono

    def prezzo_totale_carrello(self):
        prezzo=0
        for prodotto in self.get_carrello_cliente():
            prezzo+=ControllerProdotto(prodotto).get_prezzo()
        return prezzo
    def get_prodotto_carrello_by_index(self,index):
        return self.model.carrello[index]
