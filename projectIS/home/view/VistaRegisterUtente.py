
from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from utilizzatore.model.Cliente import Cliente
class VistaRegisterUtente(QFrame):
    def __init__(self,controller):
        super(VistaRegisterUtente,self).__init__()
        uic.loadUi('home/view/vistaregisterutente.ui',self)
        self.controller = controller
        self.reg_cliente_button.clicked.connect(self.registra_Cliente)

    def closeEvent(self, event):
        self.controller.save_data()
    def registra_Cliente(self):
        nome = self.textNome.text()
        cognome = self.textCognome.text()
        email = self.textEmail.text()
        password = self.textPassword.text()
        cpassword = self.textCPassword.text()
        telefono = self.textTelefono.text()
        if len(nome) == 0 or len(cognome) == 0 or len(email) == 0 or len(password) == 0 or len(cpassword)== 0 or len(telefono) == 0:
            self.error.setText("alcuni campi non sono compilati")
        elif password!=cpassword:
            self.error.setText("le password non coincidono")
        else:
            self.controller.aggiungi_cliente(Cliente(
                nome,
                cognome,
                email,
                password,
                telefono,
                )
            )
            self.close()










