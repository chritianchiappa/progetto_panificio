from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from dipendente.model.Dipendente import Dipendente
from validazionecampi.validazione_campi import Validation
class VistaInserisciDipendente(QWidget):
    def __init__(self ,controller,callback):
        super(VistaInserisciDipendente, self).__init__()
        uic.loadUi('listadipendenti/view/vistainseriscidipendente.ui', self)
        self.setWindowTitle("Inserisci dipendente")
        self.controller = controller
        self.callback = callback
        self.reg_dip_button.clicked.connect(self.registra_Dipendente)
    def registra_Dipendente(self):
        id = self.id.text().strip()
        nome = self.nome.text().strip()
        cognome = self.cognome.text().strip()
        cfiscale= self.cfiscale.text().strip()
        indirizzo= self.indirizzo.text().strip()
        telefono = self.telefono.text().strip()
        val = Validation()
        if len(nome) == 0 or len(cognome) == 0 or len(id) == 0 or len(cfiscale) == 0 or len(indirizzo) == 0 or len(telefono) == 0:
            self.error.setText("Alcuni campi non sono compilati")
        elif self.controller.check_dipendente_by_id(id):
            self.error.setText("Un altro dipendente possiede gia questo id")
        elif val.val_cfiscale(cfiscale):
            self.error.setText("Codice fiscale non valido")
        elif val.val_telefono(telefono):
            self.error.setText("Numero di telefono non esistente")

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
                []
                )
            )
            self.callback()
            self.controller.save_data()
            self.close()