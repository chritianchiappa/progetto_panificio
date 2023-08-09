from utilizzatore.model.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):
    def __init__(self, nome, cognome, email, password,telefono):
        super(Cliente, self).__init__(nome, cognome, email, password)
        self.telefono=telefono
    def check_cliente(self, email,password):
        if self.email == email and self.password == password:
            return True
        else:
            return False