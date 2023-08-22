from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import  QTimer, Qt

import webbrowser
from datetime import datetime
class HomeCliente(QWidget):
    def __init__(self,cliente):
        super(HomeCliente,self).__init__()
        uic.loadUi('utilizzatore/view/vistaCliente.ui',self)
        self.setWindowTitle("Home")
        self.cliente=cliente
        self.carrello_button.clicked.connect(self.go_Lista_Ordini)
        self.whishlist_button.clicked.connect(self.go_Magazzino)
        self.shop_button.clicked.connect(self.go_Prodotti)
        self.torte_button.clicked.connect(self.go_Torte)
        self.Data.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.Ora.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.logo_button.clicked.connect(self.open_sito)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def open_sito(self):
        webbrowser.open(
            "https://www.tripadvisor.it/Restaurant_Review-g1934128-d15861838-Reviews-Il_Piccolo_Forno-Castelplanio_Province_of_Ancona_Marche.html")

    def update_time(self):
        time=datetime.now()
        formatted_time= time.strftime("%H:%M:%S")
        formatted_data=time.strftime("%d/%m/%Y")
        self.Ora.setText(formatted_time)
        self.Data.setText(formatted_data)

    def go_Lista_Ordini(self):
        self.close()
    def go_Torte(self):
        self.close()
    def go_Magazzino(self):
        #self.VistaIng=VistaIngredienti()
        #self.VistaIng.show()
        self.close()
    def go_Prodotti(self):
        self.close()
