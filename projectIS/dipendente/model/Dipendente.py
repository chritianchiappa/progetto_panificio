from utilizzatore.model.Utilizzatore import Utilizzatore

class Dipendente(Utilizzatore):
    def __init__(self, nome, cognome, email, password,cfiscale,indirizzo,id,telefono,notifiche):
        super(Dipendente, self).__init__(nome, cognome, email, password)
        self.cfiscale=cfiscale
        self.indirizzo=indirizzo
        self.id=id
        self.telefono=telefono
        self.notifiche=notifiche

