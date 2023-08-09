from listaclienti.model.lista_clienti import ListaClienti

class ControllerListaClienti():

    def __init__(self):
        self.model = ListaClienti()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def ritorna_nome(self,cognome):
        return self.model.ritorna_nome(cognome)

    def rimuovi_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)

    def save_data(self):
        self.model.save_data()