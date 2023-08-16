from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QTime,QTimer
from listadipendenti.view.vista_lista_dipendenti import VistaListaDipendenti
import webbrowser
from datetime import datetime
class HomeAmministratore(QWidget):
    def __init__(self):
        super(HomeAmministratore,self).__init__()
        uic.loadUi('utilizzatore/view/vistaAmministratore.ui',self)
        self.setWindowTitle("Home")
        self.dipendenti_button.clicked.connect(self.go_Lista_Dipendenti)
        self.magazzino_button.clicked.connect(self.go_Magazzino)
        self.statistiche_button.clicked.connect(self.go_Statistiche)
        self.cassa_button.clicked.connect(self.go_Cassa)
        #self.logout_button.clicked.connect(self.go_Login)
        #self.logo_button.clicked.connect(webbrowser.open("https://www.tripadvisor.it/Restaurant_Review-g1934128-d15861838-Reviews-Il_Piccolo_Forno-Castelplanio_Province_of_Ancona_Marche.html"))
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        time=datetime.now()
        formatted_time= time.strftime("%H:%M:%S")
        formatted_data=time.strftime("%d/%m/%Y")
        self.lcdOra.setDigitCount(8)
        self.lcdOra.display(formatted_time)
        self.Data.setText(formatted_data)

    def go_Lista_Dipendenti(self):
        self.VistaDip = VistaListaDipendenti()
        self.VistaDip.show()
    def go_Magazzino(self):
        self.close()
    def go_Statistiche(self):
        self.close()
    def go_Cassa(self):
        self.close()