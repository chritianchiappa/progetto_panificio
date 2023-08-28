from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from prodotto.controller.ControllerProdotto import ControllerProdotto
from cliente.controller.ControllerCliente import ControllerCliente

class VistaProdotto(QWidget):
    def __init__(self,prodotto,cliente,lista_prodotti):
        super(VistaProdotto, self).__init__()
        uic.loadUi('prodotto/view/vistaProdotto.ui', self)
        self.cliente=cliente
        self.prodotto=prodotto
        self.controller_prodotto = ControllerProdotto(prodotto)
        self.controller_cliente = ControllerCliente(cliente)
        self.lista_prodotti = lista_prodotti
        self.lista_ingredienti = self.controller_prodotto.get_lista_ingredienti()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.controlla_like()
        self.nome.setText(self.prodotto.nome)
        self.prezzo.setText(f"{self.prodotto.prezzo} €")
        self.agg_carrello_button.clicked.connect(self.aggiungi_al_carrello)
        self.acquista_button.clicked.connect(self.acquista)
        self.like_button.clicked.connect(self.aggiungi_whishlist)
        self.dettagli_button.clicked.connect(self.mostra_dettagli)

    def aggiungi_al_carrello(self):
        self.controller_cliente.aggiungi_prodotto_carrello(self.prodotto)
        print(f"{self.prodotto.nome} aggiunto al carrello di {self.cliente.nome}")
    def acquista(self):
        print(f"{self.prodotto.nome} acquistato da {self.cliente.nome}")

    def aggiungi_whishlist(self):
        if self.like_button.isChecked():
            self.cliente.whishlist.append(self.prodotto)
        else:
            self.cliente.whishlist.remove(self.prodotto)
        print(f"{self.prodotto.nome} aggiunto a Whishlist di {self.cliente.nome}")

    def mostra_dettagli(self):
        for ingrediente in self.lista_ingredienti:
            print(ingrediente.nome)
    def controlla_like(self):
        for prodotto_liked in self.controller_cliente.get_whishlist_cliente():
            print(prodotto_liked.nome)
            if self.prodotto==prodotto_liked:
                self.like_button.setChecked(True)


