class ControllerProdotto:
    def __init__(self,prodotto):
        self.model = prodotto

    def get_lista_ingredienti(self):
        return self.model.ingredienti