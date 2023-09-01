from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import  QTimer, Qt,QPropertyAnimation,QEasingCurve

import webbrowser
from datetime import datetime

from listaordini.view.vista_lista_ordini import VistaListaOrdini


class HomeDipendente(QWidget):
    def __init__(self,login,dipendente):
        super(HomeDipendente,self).__init__()
        uic.loadUi('utilizzatore/view/vistaDipendente.ui',self)
        self.setWindowTitle("Home")
        self.login=login
        self.dipendente=dipendente
        self.ordini_button.clicked.connect(self.go_Lista_Ordini)
        self.prodotti_button.clicked.connect(self.go_Prodotti)
        self.open_close_side_bar_btn.clicked.connect(self.slideMenu)
        self.nome.setText(dipendente.nome)
        self.logout_button.clicked.connect(self.logout)
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

    def logout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Sei sicuro di voler effettuare il logout?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            self.close()
            self.login.show()
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

    def go_Lista_Ordini(self):
        self.VistaOrdini=VistaListaOrdini()
        self.VistaOrdini.show()

    def go_Prodotti(self):
        self.close()

    def closeEvent(self,event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Sei sicuro di voler chiudere il programma?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

