from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from utilizzatore.model.Dipendente import Dipendente

class VistaInserisciDipendente(QWidget):
    def __init__(self ,controller):
        super(VistaInserisciDipendente, self).__init__()
        uic.loadUi('listadipendenti/view/vistainseriscidipendente.ui', self)
        self.controller = controller
        self.reg_dip_button.clicked.connect(self.registra_Dipendente)
    def closeEvent(self, event):
        self.controller.save_data()
    def registra_Dipendente(self):
        id = self.idfield.text()
        nome = self.nomefield.text()
        cognome = self.cognomefield.text()
        cfiscale= self.cfiscale.text()
        indirizzo= self.indirizzo.text()
        telefono = self.telefono.text()
        if len(nome) == 0 or len(cognome) == 0 or len(id) == 0 or len(cfiscale) == 0 or len(indirizzo) == 0 or len(telefono) == 0:
            self.error.setText("alcuni campi non sono compilati")
        else:
            self.controller.aggiungi_dipendente(Dipendente(
                nome,
                cognome,
                "",
                "",
                cfiscale,
                indirizzo,
                id,
                telefono,
                )
            )
            self.close()