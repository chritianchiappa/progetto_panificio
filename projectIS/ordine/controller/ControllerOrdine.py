from prodotto.controller.ControllerProdotto import ControllerProdotto

class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_lista_prodotti_ordinati(self):
        return self.model.prodotti

    def get_cliente(self):
        return self.model.cliente

    def get_importo(self):
        importo=0
        for prodotto in self.get_lista_prodotti_ordinati():
            importo+=ControllerProdotto(prodotto).get_prezzo()

        return importo


    def get_data_ordine(self):
        return self.model.data