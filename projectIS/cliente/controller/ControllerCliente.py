from prodotto.controller.ControllerProdotto import ControllerProdotto

class ControllerCliente():
    def __init__(self, cliente):
        self.model = cliente


    def get_nome_cliente(self):
        return str(self.model.nome)

    def get_email(self):
        return str(self.model.email)
    def get_password(self):
        return str(self.model.password)

    def get_telefono(self):
        return str(self.model.telefono)

    def set_nome_cliente(self,nome):
        self.model.nome=nome

    def get_cognome_cliente(self):
        return str(self.model.cognome)

    def get_carrello_cliente(self):
        return self.model.carrello

    def aggiungi_prodotto_carrello(self,prodotto,quantita):

        for elemento in self.get_carrello_cliente():
            if prodotto.nome==elemento.nome:
                ControllerProdotto(elemento).set_quantita(elemento.quantita + quantita)
                return
        ControllerProdotto(prodotto).set_quantita(quantita)
        self.model.carrello.append(prodotto)

    def rimuovi_prodotto_carrello_index(self,index):
        self.model.carrello.pop(index)
    def rimuovi_prodotto_carrello(self,prodotto):
        self.model.carrello.remove(prodotto)
    def rimuovi_prodotto_whishlist_index(self,index):
        self.model.whishlist.pop(index)

    def aggiungi_prodotto_whishlist(self,prodotto):
        self.model.whishlist.append(prodotto)

    def rimuovi_prodotto_whishlist(self,prodotto_c):
        for prodotto in self.get_whishlist_cliente():
            if prodotto_c.nome== prodotto.nome:
                self.model.whishlist.remove(prodotto)
    def get_whishlist_cliente(self):
        return self.model.whishlist
    def prezzo_totale_carrello(self):
        prezzo=0
        for prodotto in self.get_carrello_cliente():
            prezzo+=ControllerProdotto(prodotto).get_prezzo()
        return prezzo
    def get_prodotto_carrello_by_index(self,index):
        return self.model.carrello[index]
    def aggiungi_notifica(self,notifica):
        self.model.notifiche.append(notifica)

    def get_lista_notifiche(self):
        return self.model.notifiche
    def get_notifica_by_index(self,index):
        return self.model.notifiche[index]
    def rimuovi_notifica_by_index(self,index):
        self.model.notifiche.pop(index)
