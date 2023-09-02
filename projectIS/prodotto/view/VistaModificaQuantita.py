from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
from prodotto.controller.ControllerProdotto import ControllerProdotto

class VistaModificaQuantita(QWidget):
    def __init__(self,magazzino,prodotto,controller_prodotti):
        super(VistaModificaQuantita, self).__init__()
        uic.loadUi('prodotto/view/VistaModificaQuantita.ui', self)
        self.conferma_button.clicked.connect(lambda: self.conferma_modifica(prodotto))
        self.controllerprod=controller_prodotti
        self.magazzino=magazzino


    def conferma_modifica(self,prodotto):

        quantita_immessa=self.le_quantita.text().strip()

        ControllerProdotto(prodotto).set_quantita(int(quantita_immessa))
        self.controllerprod.save_data()
        self.popup()
        self.magazzino.update_list_prodotti()
        self.close()


    def popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Quantita aggiornata con successo")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()


