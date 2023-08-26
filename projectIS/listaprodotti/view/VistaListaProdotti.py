from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from prodotto.view.VistaProdotto import VistaProdotto
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
class VistaListaProdotti(QWidget):
    def __init__(self,cliente):
        super(VistaListaProdotti, self).__init__()
        uic.loadUi('listaprodotti/view/vistaListaProdotti.ui', self)
        self.cliente=cliente
        self.setWindowTitle("Shop")
        self.controller_lista_prodotti = ControllerListaProdotti()
        self.controller_lista_clienti = ControllerListaClienti()
        self.lista_prodotti = self.controller_lista_prodotti.get_lista_prodotti()
        self.popola_shop()
    def aggiungi_prodotto(self,rowNumber,columnNumber,prodotto):
        self.widget_prodotto=VistaProdotto(prodotto,self.cliente,self.lista_prodotti)
        self.gridLayout.addWidget(self.widget_prodotto,rowNumber,columnNumber,1,1,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

    def popola_shop(self):
        col=0
        row=0
        for prodotto in self.lista_prodotti:
            self.aggiungi_prodotto(row,col,prodotto)
            col += 1
            if col >= 3:
                col = 0
                row += 1
    def popup_quantita_insufficiente(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText("Quantita dei prodotti insufficiente")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes)
        msg.setDefaultButton(QMessageBox.StandardButton.Yes)
        msg.exec()
    def closeEvent(self, event):
        self.controller_lista_clienti.save_data()





