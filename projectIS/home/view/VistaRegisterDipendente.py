from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from utilizzatore.model.Dipendente import Dipendente
from validazionecampi.validazione_campi import Validation


class VistaRegisterDipendente(QFrame):
    def __init__(self,controller):
        super(VistaRegisterDipendente,self).__init__()
        uic.loadUi('home/view/vistaregisterdipendente.ui',self)
        self.controller = controller
        self.cc_button.clicked.connect(self.reg_dipendente)

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
            else:
                self.error.setText("Dipendente non trovato")





