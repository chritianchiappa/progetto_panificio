from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from amministratore.model.Amministratore import Amministratore
from amministratore.view.HomeAmministratore import HomeAmministratore

class VistaLogAmm(QFrame):
    def __init__(self,login,controller,controllerdip):
        super(VistaLogAmm, self).__init__()
        uic.loadUi('amministratore/view/vistalogamm.ui', self)
        self.login=login
        self.controller=controller
        self.controllerdip=controllerdip
        self.la_button.clicked.connect(self.go_HomeAmm)

    def go_HomeAmm(self):
        idamm=self.Id_field.text()
        if Amministratore.id!=idamm:  #controllo che l' id immesso corrisponda a quello dell amministratore
            self.error.setText("Id non corretto!")
        else:
            self.close()
            self.login.hide()
            self.home=HomeAmministratore(self.login,self.controller,self.controllerdip)
            self.home.show()



