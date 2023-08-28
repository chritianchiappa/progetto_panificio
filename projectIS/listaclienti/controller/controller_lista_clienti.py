from listaclienti.model.lista_clienti import ListaClienti

class ControllerListaClienti():

    def __init__(self):
        self.model = ListaClienti()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def aggiorna_carrello_cliente(self,cliente,carrello):
        self.model.aggiorna_carrello_cliente(cliente,carrello)

    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def check_cliente(self,email,password):
        return self.model.check_cliente(email,password)

    def ritorna_nome(self,cognome):
        return self.model.ritorna_nome(cognome)

    def rimuovi_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)

    def save_data(self):
        self.model.save_data()