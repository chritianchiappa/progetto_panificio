from prodotto.controller.ControllerProdotto import ControllerProdotto

class ControllerCliente():
    def __init__(self, cliente):
        self.model = cliente


    def get_nome_cliente(self):
        return str(self.model.nome)

    def set_nome_cliente(self,nome):
        self.model.nome=nome

    def get_cognome_cliente(self):
        return str(self.model.cognome)

    def get_carrello_cliente(self):
        return self.model.carrello

    def aggiungi_prodotto_carrello(self,prodotto):
        self.model.carrello.append(prodotto)

    def aggiungi_prodotto_whishlist(self,prodotto):
        self.model.whishlist.append(prodotto)

    def rimuovi_prodotto_whishlist(self,prodotto_c):
        for prodotto in self.get_whishlist_cliente():
            if prodotto_c.nome== prodotto.nome:
                self.model.whishlist.remove(prodotto)
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
