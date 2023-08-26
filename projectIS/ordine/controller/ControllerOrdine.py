class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_lista_prodotti_ordinati(self):
        return self.model.prodotti

    def get_cliente(self):
        return self.model.cliente

    def get_importo(self):
        return self.model.importo

    def get_data_ordine(self):
        return self.model.data