from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from listadipendenti.view.vista_lista_dipendenti import VistaListaDipendenti
class VistaAmministratore(QWidget):
    def __init__(self):
        super(VistaAmministratore,self).__init__()
        uic.loadUi('utilizzatore/view/vistaAmministratore.ui',self)
        self.setWindowTitle("Home")
        self.dipendenti_button.clicked.connect(self.go_Lista_Dipendenti)
        self.magazzino_button.clicked.connect(self.go_Magazzino)
        self.statistiche_button.clicked.connect(self.go_Statistiche)
        self.cassa_button.clicked.connect(self.go_Cassa)

    def go_Lista_Dipendenti(self):
        self.VistaDip = VistaListaDipendenti()
        self.VistaDip.show()

    def go_Magazzino(self):
        self.close()
    def go_Statistiche(self):
        self.close()
    def go_Cassa(self):
        self.close()