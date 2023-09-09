from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
import os
from PyQt6.QtGui import QPixmap,QPainter, QPainterPath

from prodotto.controller.ControllerProdotto import ControllerProdotto
from cliente.controller.ControllerCliente import ControllerCliente


class VistaProdotto(QWidget):
    def __init__(self,prodotto,cliente,controller_prodotti):
        super(VistaProdotto, self).__init__()
        uic.loadUi('prodotto/view/vistaProdotto.ui', self)
        self.cliente=cliente
        self.prodotto=prodotto
        self.controller_prodotto = ControllerProdotto(prodotto)
        self.controller_cliente = ControllerCliente(cliente)
        self.controller_prodotti=controller_prodotti
        self.lista_ingredienti = self.controller_prodotto.get_lista_ingredienti()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.controlla_like()
        self.popola_combobox()
        self.mostra_immagine()
        self.nome.setText(self.prodotto.nome)
        self.prezzo.setText(f"{self.prodotto.prezzo} €")
        self.agg_carrello_button.clicked.connect(self.aggiungi_al_carrello)

        self.like_button.clicked.connect(self.aggiungi_whishlist)
        self.dettagli_button.clicked.connect(self.mostra_dettagli)

    def popola_combobox(self):
        self.selettore_quantita.clear()
        quantita_disponibile = int(self.prodotto.quantita)

        # Aggiungi le opzioni solo se la quantità è maggiore di 0
        if quantita_disponibile > 0:
            for quantita in range(1, quantita_disponibile + 1):
                self.selettore_quantita.addItem(str(quantita))
        else:
            self.selettore_quantita.addItem("Esaurito")
            self.agg_carrello_button.setDisabled(False)

    def mostra_immagine(self):
        if os.path.isfile('immagini/' + str(self.prodotto.nome) + '.png'):
            pixmap = QPixmap('immagini/' + str(self.prodotto.nome) + '.png')
        else:
            pixmap = QPixmap('immagini/noimage.png')
        pixmap_scaled = pixmap.scaled(320, 220, Qt.AspectRatioMode.KeepAspectRatio)

        self.immagine_prodotto.setPixmap(pixmap_scaled)


    def aggiungi_al_carrello(self):
        quantita_selezionata = int(self.selettore_quantita.currentText())
        prodotto_copia = self.prodotto.copia()
        self.controller_cliente.aggiungi_prodotto_carrello(prodotto_copia,quantita_selezionata)
        self.popup(f"{self.prodotto.nome} aggiunto al carrello",QMessageBox.Icon.Information)



    def aggiungi_whishlist(self):
        if self.like_button.isChecked():
            self.controller_cliente.aggiungi_prodotto_whishlist(self.prodotto)
        else:
            self.controller_cliente.rimuovi_prodotto_whishlist(self.prodotto)
        print(f"{self.prodotto.nome} aggiunto a Whishlist di {self.cliente.nome}")

    def mostra_dettagli(self):
        for ingrediente in self.lista_ingredienti:
            print(ingrediente.nome)

    def controlla_like(self):
        for prodotto_liked in self.controller_cliente.get_whishlist_cliente():
            if self.prodotto.nome==prodotto_liked.nome:
                self.like_button.setChecked(True)

    def popup(self, text, icon):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()
