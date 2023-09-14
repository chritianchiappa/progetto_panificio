
from PyQt6.QtWidgets import QWidget,QLineEdit,QMessageBox
from PyQt6 import uic
from cliente.model.Cliente import Cliente
from validazionecampi.validazione_campi import Validation
from PyQt6.QtGui import QPixmap,QPalette,QBrush
class VistaRegisterUtente(QWidget):
    def __init__(self,controller):
        super(VistaRegisterUtente,self).__init__()
        uic.loadUi('cliente/view/vistaregisterutente.ui',self)
        self.setWindowTitle("Registrazione utente")
        self.controller = controller


        self.sp_button.clicked.connect(self.show_password)
        self.scp_button.clicked.connect(self.show_cpassword)
        self.reg_cliente_button.clicked.connect(self.registra_Cliente)

    def show_password(self):
        if self.sp_button.isChecked():
            self.textPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.textPassword.setEchoMode(QLineEdit.EchoMode.Password)

    def show_cpassword(self):
        if self.scp_button.isChecked():
            self.textCPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.textCPassword.setEchoMode(QLineEdit.EchoMode.Password)



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
            self.error.setText("password non valida")
        elif val.val_telefono(telefono):
            self.error.setText("numero di telefono non esistente")
        elif self.controller.check_email(email):
            self.error.setText("Un account è gia registrato con questa email")
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
            self.popup()
            self.close()

    def popup(self):
        msg = QMessageBox()
        msg.setText("Registrazione avvenuta con successo")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()










