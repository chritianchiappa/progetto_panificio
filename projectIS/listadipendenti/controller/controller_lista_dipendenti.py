from listadipendenti.model.lista_dipendenti import ListaDipendenti

class ControllerListaDipendenti():

    def __init__(self):
        self.model = ListaDipendenti()

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    def get_lista_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def check_dipendente_by_id(self, id):
        self.model.check_dipendente_by_id(id)

    def rimuovi_dipendente_by_id(self, id):
        self.model.rimuovi_dipendente_by_id(id)

    def save_data(self):
        self.model.save_data()