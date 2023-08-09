from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from utilizzatore.view.vista_inserisci_dipendente import VistaInserisciDipendente

class VistaListaDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)
        uic.loadUi('listadipendenti/view/vistalistadipendenti.ui', self)
        self.new_button.clicked.connect(self.show_new_dipendente)
    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente()
        self.vista_inserisci_dipendente.show()


