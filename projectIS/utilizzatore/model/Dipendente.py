from utilizzatore.model.Amministratore import Amministratore

class Dipendente(Amministratore):
    def __init__(self, nome, cognome, email, password, datanascita,luogonascita,id,telefono):
        super(Dipendente, self).__init__(nome, cognome, email, password, datanascita,luogonascita,id,telefono)
