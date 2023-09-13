from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QTimer,QPropertyAnimation,QEasingCurve
from listadipendenti.view.vista_lista_dipendenti import VistaListaDipendenti
import webbrowser
from datetime import datetime
from notifica.view.InviaNotifica import InviaNotifica
from statistiche.view.VistaStatistiche import VistaStatistiche
from listaordini.view.VistaCassa import VistaCassa


class HomeAmministratore(QWidget):
    def __init__(self,login,controller,controllerdip):
        super(HomeAmministratore,self).__init__()
        uic.loadUi('amministratore/view/vistaAmministratore.ui',self)
        self.setWindowTitle("Home")
        self.login=login

        self.controller=controller
        self.controllerdip=controllerdip
        self.logout_requested = False
        self.open_close_side_bar_btn.clicked.connect(self.slideMenu)
        self.dipendenti_button.clicked.connect(self.go_Lista_Dipendenti)

        self.statistiche_button.clicked.connect(self.go_Statistiche)
        self.cassa_button.clicked.connect(self.go_Cassa)
        self.logout_button.clicked.connect(self.logout)
        self.logo_button.clicked.connect(self.open_sito)
        self.notifiche_button.clicked.connect(self.crea_notifica)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def open_sito(self):
        webbrowser.open(
            "https://www.tripadvisor.it/Restaurant_Review-g1934128-d15861838-Reviews-Il_Piccolo_Forno-Castelplanio_Province_of_Ancona_Marche.html")

    def update_time(self):
        time = datetime.now()
        formatted_time = time.strftime("%H:%M:%S")
        formatted_data = time.strftime("%d/%m/%Y")
        self.Ora.setText(formatted_time)
        self.Data.setText(formatted_data)

    def logout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Sei sicuro di voler effettuare il logout?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            self.logout_requested=True
            self.login.clear_fields()
            self.login.show()
            self.close()
    def crea_notifica(self):
        self.SendNot=InviaNotifica(self.controller,self.controllerdip)
        self.SendNot.show()

    def slideMenu(self):
        self.animation = QPropertyAnimation(self.slide_menu, b"maximumWidth")
        self.animation.setDuration(250)
        easing_curve = QEasingCurve(QEasingCurve.Type.Linear)
        if self.open_close_side_bar_btn.isChecked():
            self.animation.setStartValue(0)
            self.animation.setEndValue(200)
            self.animation.setEasingCurve(easing_curve)
            self.animation.start()
        else:
            self.animation.setStartValue(200)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(easing_curve)
            self.animation.start()

    def go_Lista_Dipendenti(self):
        self.VistaDip = VistaListaDipendenti(self.controllerdip)
        self.VistaDip.show()

    def go_Statistiche(self):
        self.stats= VistaStatistiche()
        self.stats.show()

    def go_Cassa(self):
        self.Cassa=VistaCassa()
        self.Cassa.show()
    def closeEvent(self, event):
        if self.logout_requested:
            event.accept()  # La finestra verrà chiusa senza popup di conferma
        else:
            # L'utente sta chiudendo la finestra normalmente, quindi mostriamo il popup di conferma
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText("Sei sicuro di voler chiudere il programma?")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            result = msg.exec()

            if result == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()