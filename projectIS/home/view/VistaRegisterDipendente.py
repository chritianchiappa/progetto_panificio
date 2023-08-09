from PyQt6.QtWidgets import QFrame
from PyQt6 import uic

class VistaRegisterDipendente(QFrame):
    def __init__(self):
        super(VistaRegisterDipendente,self).__init__()
        uic.loadUi('home/view/vistaregisterdipendente.ui',self)
        self.cc_button.clicked.connect(self.go_Login)
    def go_Login(self):
        self.close()