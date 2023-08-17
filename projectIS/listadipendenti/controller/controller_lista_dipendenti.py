from listadipendenti.model.lista_dipendenti import ListaDipendenti

class ControllerListaDipendenti():

    def __init__(self):
        self.model = ListaDipendenti()

    def aggiorna_dipendente(self, id,email, password):
        dipendente = self.model.check_dipendente_by_id(id)
        dipendente.email=email
        dipendente.password=password
        self.model.save_data()


    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    def rimuovi_dipendente_by_index(self,index):
        self.model.rimuovi_dipendente_by_index(index)

    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)

    def get_lista_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def check_dipendente_by_id(self, id):
        return self.model.check_dipendente_by_id(id)

    def rimuovi_dipendente_by_id(self, id):
        self.model.rimuovi_dipendente_by_id(id)

    def save_data(self):
        self.model.save_data()