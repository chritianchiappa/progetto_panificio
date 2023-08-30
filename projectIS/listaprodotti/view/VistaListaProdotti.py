from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from prodotto.view.VistaProdotto import VistaProdotto
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
class VistaListaProdotti(QWidget):
    def __init__(self,cliente,controller):
        super(VistaListaProdotti, self).__init__()
        uic.loadUi('listaprodotti/view/vistaListaProdotti.ui', self)
        self.cliente=cliente
        self.setWindowTitle("Shop")
        self.controller_lista_prodotti = ControllerListaProdotti()
        self.controller_lista_clienti=controller
        self.lista_prodotti = self.controller_lista_prodotti.get_lista_prodotti()
        self.lista_prodotti_filtrata = self.lista_prodotti[:]
        self.popola_shop(self.lista_prodotti)
        self.filtro_prodotti.activated.connect(self.filtro_tipologia)
        self.cerca_button.clicked.connect(self.ricerca)
    def aggiungi_prodotto(self,rowNumber,columnNumber,prodotto):
        self.widget_prodotto=VistaProdotto(prodotto,self.cliente,self.controller_lista_prodotti)
        self.gridLayout.addWidget(self.widget_prodotto,rowNumber,columnNumber,1,1,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

    def popola_shop(self,lista):
        col=0
        row=0
        for prodotto in lista:
            print(prodotto.nome + str(prodotto.quantita))
            self.aggiungi_prodotto(row,col,prodotto)
            col += 1
            if col >= 3:
                col = 0
                row += 1

    def ricerca(self):
        nome_prodotto = self.cerca_prodotto.text()
        if len(nome_prodotto) == 0:
            self.popup_ricerca("Immetti qualcosa per la ricerca")
        else:
            prodotti_trovati = [prodotto for prodotto in self.lista_prodotti if
                                nome_prodotto.lower() in prodotto.nome.lower()]
            if prodotti_trovati:
                self.clear_layout(self.gridLayout)
                self.popola_shop(prodotti_trovati)
            else:
                self.popup_ricerca("Nessun prodotto trovato con questo nome")

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    def filtro_tipologia(self):
        filtro_tipo=self.filtro_prodotti.currentText()
        if filtro_tipo == "Tutti":
            self.lista_prodotti_filtrata = self.lista_prodotti[:]
        else:
            self.lista_prodotti_filtrata = [prodotto for prodotto in self.lista_prodotti if
                                            prodotto.tipo == filtro_tipo]
        self.clear_layout(self.gridLayout)
        self.popola_shop(self.lista_prodotti_filtrata)


    def popup_quantita_insufficiente(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText("Quantita dei prodotti insufficiente")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes)
        msg.setDefaultButton(QMessageBox.StandardButton.Yes)
        msg.exec()
    def popup_ricerca(self,testo):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(testo)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()


    def closeEvent(self, event):
        self.controller_lista_clienti.aggiorna_carrello_cliente(self.cliente.email,self.cliente.password,self.cliente.carrello)
        self.controller_lista_clienti.aggiorna_whishlist_cliente(self.cliente.email,self.cliente.password,self.cliente.whishlist)
        self.controller_lista_clienti.save_data()





