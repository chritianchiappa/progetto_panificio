from PyQt6.QtWidgets import QWidget
from PyQt6 import uic



class VistaListaProdotti(QWidget):
    def __init__(self):
        super(VistaListaProdotti, self).__init__()
        uic.loadUi('listaprodotti/view/vistaListaProdotti.ui', self)
        self.setWindowTitle("Shop")


