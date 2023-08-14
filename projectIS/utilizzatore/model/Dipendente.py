from utilizzatore.model.Utilizzatore import Utilizzatore

class Dipendente(Utilizzatore):
    def __init__(self, nome, cognome, email, password,cfiscale,indirizzo,id,telefono):
        super(Dipendente, self).__init__(nome, cognome, email, password)
        self.cfiscale=cfiscale
        self.indirizzo=indirizzo
        self.id=id
        self.telefono=telefono

    def modifica_email_password(self,email,password):
        self.email=email
        self.password=password