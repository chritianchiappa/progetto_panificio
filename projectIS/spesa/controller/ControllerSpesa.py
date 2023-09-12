class ControllerSpesa:
    def __init__(self, spesa):
        self.model = spesa

    def get_nome_ingrediente(self):
        return self.model.ingrediente.nome
    def get_costo_ingrediente(self):
        return self.model.ingrediente.prezzo*self.model.ingrediente.quantita
    def get_data(self):
        return self.model.data
