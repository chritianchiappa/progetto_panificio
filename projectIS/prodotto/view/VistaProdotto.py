from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class VistaProdotto(QWidget):
    def __init__(self,prodotto,cliente):
        super(VistaProdotto, self).__init__()
        uic.loadUi('prodotto/view/vistaProdotto.ui', self)
        self.cliente=cliente
        self.prodotto=prodotto
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.nome.setText(self.prodotto.nome)
        self.prezzo.setText(f"{self.prodotto.prezzo} €")
        self.agg_carrello_button.clicked.connect(self.aggiungi_al_carrello)
        self.acquista_button.clicked.connect(self.acquista)

    def aggiungi_al_carrello(self):
        #self.cliente.carrello.append(self.prodotto)
        print(f"{self.prodotto.nome} aggiunto al carrello di {self.cliente.nome}")
    def acquista(self):
        print(f"{self.prodotto.nome} aacquistato da {self.cliente.nome}")