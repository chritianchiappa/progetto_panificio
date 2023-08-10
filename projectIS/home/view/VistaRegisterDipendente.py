from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from utilizzatore.model.Dipendente import Dipendente

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
        dipendente_cercato=self.controller.check_dipendente_by_id(id)
        print(dipendente_cercato.nome)
        if len(email) == 0 or len(password) == 0 or len(cpassword) == 0:
            self.error.setText("alcuni campi non sono compilati")
        elif password != cpassword:
            self.error.setText("le password non coincidono")
        if dipendente_cercato:
            dipendente_cercato.email = email
            dipendente_cercato.password = password
            self.close()
        else:
            self.error.setText("non esiste un dipendente con tale id")
