from prodotto.controller.ControllerProdotto import ControllerProdotto
from cliente.controller.ControllerCliente import ControllerCliente
class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_lista_prodotti_ordinati(self):
        return self.model.prodotti

    def get_nome_cliente(self):
        return ControllerCliente(self.model.cliente).get_nome_cliente

    def get_cognome_cliente(self):
        return ControllerCliente(self.model.cliente).get_cognome_cliente
    def get_importo(self):
        importo=0
        for prodotto in self.get_lista_prodotti_ordinati():
            importo+=ControllerProdotto(prodotto).get_prezzo()

        return importo


    def get_data_ordine(self):
        return self.model.data