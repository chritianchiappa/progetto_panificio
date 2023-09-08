
from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from cliente.model.Cliente import Cliente
from validazionecampi.validazione_campi import Validation
class VistaRegisterUtente(QFrame):
    def __init__(self,controller):
        super(VistaRegisterUtente,self).__init__()
        uic.loadUi('home/view/vistaregisterutente.ui',self)
        self.controller = controller
        self.reg_cliente_button.clicked.connect(self.registra_Cliente)



    def registra_Cliente(self):
        nome = self.textNome.text()
        cognome = self.textCognome.text()
        email = self.textEmail.text()
        password = self.textPassword.text()
        cpassword = self.textCPassword.text()
        telefono = self.textTelefono.text()
        val=Validation()
        if len(nome) == 0 or len(cognome) == 0 or len(email) == 0 or len(password) == 0 or len(cpassword)== 0 or len(telefono) == 0:
            self.error.setText("alcuni campi non sono compilati")
        elif val.val_email(email):
            self.error.setText("email non valida")
        elif password != cpassword:
            self.error.setText("le password non coincidono")
        elif val.val_password(password):
            self.error.setText("La password deve contenere almeno 8 caratteri, una lettera maiuscola, una lettera "
                               "minuscola e un numero")
        elif val.val_telefono(telefono):
            self.error.setText("numero di telefono non esistente")
        else:
            self.controller.aggiungi_cliente(Cliente(
                nome,
                cognome,
                email,
                password,
                telefono,
                [],
                [],
                []
                )
            )
            self.controller.save_data()
            self.close()










