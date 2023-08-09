from PyQt6.QtWidgets import QFrame
from PyQt6 import uic
from utilizzatore.model.Amministratore import Amministratore

class VistaLogAmm(QFrame):
    def __init__(self,login,home):
        super(VistaLogAmm, self).__init__()
        uic.loadUi('home/view/vistalogamm.ui', self)
        self.login=login;
        self.home=home;
        self.la_button.clicked.connect(self.go_HomeAmm)

    def go_HomeAmm(self):
        idamm=self.Id_field.text()
        if Amministratore.id!=idamm:
            self.error.setText("Id non corretto!")
        else:
            self.close()
            self.login.close()
            self.home.show()



