from PyQt6.QtWidgets import QFrame, QLineEdit, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt

from validazionecampi.validazione_campi import Validation


class VistaRegisterDipendente(QFrame):
    def __init__(self,controller):
        super(VistaRegisterDipendente,self).__init__()
        uic.loadUi('home/view/vistaregisterdipendente.ui',self)
        self.controller = controller
        self.registrati_button.clicked.connect(self.reg_dipendente)
        self.sp_button.clicked.connect(self.show_password)
        self.scp_button.clicked.connect(self.show_cpassword)
        self.error.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

    def show_password(self):
        if self.sp_button.isChecked():
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def show_cpassword(self):
        if self.scp_button.isChecked():
            self.cpassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.cpassword.setEchoMode(QLineEdit.EchoMode.Password)
    def closeEvent(self, event):
        self.controller.save_data()

    def reg_dipendente(self):
        id=self.id.text()
        email = self.email.text()
        password = self.password.text()
        cpassword = self.cpassword.text()
        val=Validation()

        if len(email) == 0 or len(password) == 0 or len(cpassword) == 0:
            self.error.setText("alcuni campi non sono compilati")
        elif val.val_email(email):
            self.error.setText("email non valida")
        elif password != cpassword:
            self.error.setText("le password non coincidono")
        elif val.val_password(password):
            self.error.setText("La password deve contenere almeno 8 caratteri, una lettera maiuscola, una lettera "
                               "minuscola e un numero")
        else:
            dipendente_cercato= self.controller.check_dipendente_by_id(id)
            if dipendente_cercato:
                self.controller.aggiorna_dipendente(id, email, password)
                msg = QMessageBox()
                msg.setText(
                    "Registrazione avvenuta con successo!")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
            else:
                self.error.setText("dipendente non trovato")





