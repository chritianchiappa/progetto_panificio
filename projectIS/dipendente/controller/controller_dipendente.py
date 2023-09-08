class ControllerDipendente():
    def __init__(self, dipendente):
        self.model = dipendente

    def get_nome_dipendente(self):
        return str(self.model.nome)

    def get_cognome_dipendente(self):
        return str(self.model.cognome)

    def get_id_dipendente(self):
        return str(self.model.id)

    def get_indirizzo_dipendente(self):
        return str(self.model.indirizzo)

    def get_telefono_dipendente(self):
        return self.model.telefono

    def get_cfiscale_dipendente(self):
        return self.model.cfiscale

    def aggiungi_notifica(self, notifica):
        self.model.notifiche.append(notifica)

    def get_lista_notifiche(self):
        return self.model.notifiche

    def get_notifica_by_index(self,index):
        return self.model.notifiche[index]

    def rimuovi_notifica_by_index(self, index):
        self.model.notifiche.pop(index)