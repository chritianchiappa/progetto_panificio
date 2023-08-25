from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from prodotto.controller.ControllerProdotto import ControllerProdotto
class VistaProdotto(QWidget):
    def __init__(self,prodotto,cliente):
        super(VistaProdotto, self).__init__()
        uic.loadUi('prodotto/view/vistaProdotto.ui', self)
        self.cliente=cliente
        self.prodotto=prodotto
        self.controller_prodotto = ControllerProdotto(prodotto)
        self.lista_ingredienti = self.controller_prodotto.get_lista_ingredienti()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.nome.setText(self.prodotto.nome)
        self.prezzo.setText(f"{self.prodotto.prezzo} €")
        self.agg_carrello_button.clicked.connect(self.aggiungi_al_carrello)
        self.acquista_button.clicked.connect(self.acquista)
        self.like_button.clicked.connect(self.aggiungi_whishlist)
        self.dettagli_button.clicked.connect(self.mostra_dettagli)

    def aggiungi_al_carrello(self):
        self.cliente.carrello.append(self.prodotto)
        print(f"{self.prodotto.nome} aggiunto al carrello di {self.cliente.nome}")
    def acquista(self):
        print(f"{self.prodotto.nome} acquistato da {self.cliente.nome}")

    def aggiungi_whishlist(self):
        self.cliente.whishlist.append(self.prodotto)
        print(f"{self.prodotto.nome} aacquistato da {self.cliente.nome}")

    def mostra_dettagli(self):
        for ingrediente in self.lista_ingredienti:
            print(ingrediente.nome)
