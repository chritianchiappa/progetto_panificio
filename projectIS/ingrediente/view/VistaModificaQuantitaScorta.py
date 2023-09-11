from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox


class VistaModificaQuantitaScorta(QWidget):
    def __init__(self,magazzino,ingrediente,controller_ingredienti):
        super(VistaModificaQuantitaScorta, self).__init__()
        uic.loadUi('ingrediente/view/VistaModificaQuantitaScorta.ui', self)
        self.setWindowTitle("Gestisci quantita")
        self.conferma_button.clicked.connect(lambda: self.conferma_modifica(ingrediente))
        self.controlleringr=controller_ingredienti
        self.magazzino=magazzino


    def conferma_modifica(self,ingrediente):

        quantita_immessa=self.selettore_quantita.value()

        ingrediente.quantita=quantita_immessa
        self.controlleringr.save_data()
        self.popup()
        self.magazzino.update_list_scorte()
        self.close()


    def popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Quantita aggiornata con successo")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()

