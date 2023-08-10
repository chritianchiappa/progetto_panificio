from utilizzatore.model.Amministratore import Amministratore

class Dipendente(Amministratore):
    def __init__(self, nome, cognome, email, password,cfiscale,indirizzo,id,telefono):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = password
        self.cfiscale=cfiscale
        self.indirizzo=indirizzo
        self.id=id
        self.telefono=telefono
        #super(Dipendente, self).__init__(nome, cognome, email, password, datanascita,luogonascita,id,telefono)
