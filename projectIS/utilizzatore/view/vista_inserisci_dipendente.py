from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from utilizzatore.model.Cliente import Cliente


class VistaInserisciDipendente(QWidget):

    def __init__(self ,parent=None):
        super(VistaInserisciDipendente, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vistainseriscidipendente.ui', self)
