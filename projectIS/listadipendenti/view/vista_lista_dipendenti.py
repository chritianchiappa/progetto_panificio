from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listadipendenti.view.vista_inserisci_dipendente import VistaInserisciDipendente
from listadipendenti.controller.controller_lista_dipendenti import ControllerListaDipendenti

class VistaListaDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)
        uic.loadUi('listadipendenti/view/vistalistadipendenti.ui', self)
        self.controller = ControllerListaDipendenti()
        self.new_button.clicked.connect(self.show_new_dipendente)
    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller)
        self.vista_inserisci_dipendente.show()


