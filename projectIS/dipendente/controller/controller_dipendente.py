class ControllerDipendente():
    def __init__(self, dipendente):
        self.model = dipendente

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_id_dipendente(self):
        return self.model.id

    def get_indirizzo_dipendente(self):
        return self.model.indirizzo

    def get_telefono_dipendente(self):
        return self.model.telefono

    def get_cfiscale_dipendente(self):
        return self.model.cfiscale