from amministratore.model.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):
    def __init__(self, nome, cognome, email, password,telefono,carrello,whishlist,notifiche):
        super(Cliente, self).__init__(nome, cognome, email, password)
        self.telefono=telefono
        self.carrello=carrello
        self.whishlist=whishlist
        self.notifiche=notifiche


