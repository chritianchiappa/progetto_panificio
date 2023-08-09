import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class VistaHome(QMainWindow):
    def __init__(self):
        super(VistaHome, self).__init__()
        uic.loadUi('home/view/vistaAmministratore.ui', self)




