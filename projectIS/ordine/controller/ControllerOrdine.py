from prodotto.controller.ControllerProdotto import ControllerProdotto
from cliente.controller.ControllerCliente import ControllerCliente
class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_lista_prodotti_ordinati(self):
        return self.model.prodotti

    def get_cliente(self):
        return self.model.cliente
    def get_nome_cliente(self):
        return ControllerCliente(self.model.cliente).get_nome_cliente()

    def get_cognome_cliente(self):
        return ControllerCliente(self.model.cliente).get_cognome_cliente()

    def get_email_cliente(self):
        return ControllerCliente(self.model.cliente).get_email()
    def get_password_cliente(self):
        return ControllerCliente(self.model.cliente).get_password()

    def get_telefono_cliente(self):
        return ControllerCliente(self.model.cliente).get_telefono()
    def get_indirizzo(self):
        return self.model.indirizzo
    def get_importo(self):
        importo=0
        prodotti_ordinati=self.get_lista_prodotti_ordinati()
        if isinstance(prodotti_ordinati,list):
            for prodotto in self.get_lista_prodotti_ordinati():
                importo+=ControllerProdotto(prodotto).get_prezzo()
        else:
            importo=prodotti_ordinati.prezzo

        return importo
    def get_mese_ordine(self):
        return self.model.data.month
    def get_anno_ordine(self):
        return self.model.data.year


    def get_data_ordine(self):
        return self.model.data.strftime("%d/%m/%Y %H:%M")
    def get_data(self):
        return self.model.data
    def get_data_consegna(self):
        return self.model.data_consegna.strftime("%d/%m/%Y %H:%M")
    def completa_ordine(self):
        self.model.completato=True