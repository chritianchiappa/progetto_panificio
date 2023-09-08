from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from utilizzatore.model.Amministratore import Amministratore
from utilizzatore.view.HomeAmministratore import HomeAmministratore

class VistaLogAmm(QFrame):
    def __init__(self,login,controller,controllerdip):
        super(VistaLogAmm, self).__init__()
        uic.loadUi('home/view/vistalogamm.ui', self)
        self.login=login
        self.controller=controller
        self.controllerdip=controllerdip
        self.la_button.clicked.connect(self.go_HomeAmm)

    def go_HomeAmm(self):
        idamm=self.Id_field.text()
        if Amministratore.id!=idamm:
            self.error.setText("Id non corretto!")
        else:
            self.close()
            self.login.hide()
            self.home=HomeAmministratore(self.login,self.controller,self.controllerdip)
            self.home.show()



