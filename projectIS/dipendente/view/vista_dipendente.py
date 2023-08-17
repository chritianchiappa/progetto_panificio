from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from dipendente.controller.controller_dipendente import ControllerDipendente


class VistaDipendente(QWidget):

    def __init__(self, dipendente, parent=None):
        super(VistaDipendente, self).__init__(parent)
        uic.loadUi('dipendente/view/dipendente.ui', self)
        self.controller = ControllerDipendente(dipendente)
        self.nome_cognome_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        self.nome_cognome_label.setText(f"{self.controller.get_nome_dipendente()} {self.controller.get_cognome_dipendente()}")
        self.id_label.setText(f"Id: {self.controller.get_id_dipendente()}")
        self.indirizzo_label.setText(f"Indirizzo: {self.controller.get_indirizzo_dipendente()}")
        self.cfiscale_label.setText(f"Codice fiscale: {self.controller.get_cfiscale_dipendente()}")
        self.telefono_label.setText(f"Telefono: {self.controller.get_telefono_dipendente()}")



