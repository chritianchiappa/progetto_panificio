from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve,QTimer
from torta.view.PersonalizzaTorta import PersonalizzaTorta

from listaprodotti.view.VistaListaProdotti import VistaListaProdotti
from carrello.view.VistaCarrello import VistaCarrello
from whishlist.view.VistaWhishlist import VistaWhishlist
from notifica.view.VistaNotifica import VistaNotifica
import webbrowser
from datetime import datetime
class HomeCliente(QWidget):
    def __init__(self,login,cliente,controller,controllerprod):
        super(HomeCliente,self).__init__()
        uic.loadUi('cliente/view/vistaCliente.ui',self)
        self.setWindowTitle("Home")
        self.cliente=cliente
        self.login=login
        self.controller=controller
        self.controllerp=controllerprod
        self.logout_requested = False
        self.carrello_button.clicked.connect(lambda: self.go_carrello(cliente))
        self.whishlist_button.clicked.connect(lambda: self.go_Whishlist(cliente,self.controller))
        self.shop_button.clicked.connect(lambda: self.go_Prodotti(cliente,self.controller))
        self.torte_button.clicked.connect(self.go_Torte)
        self.logo_button.clicked.connect(self.open_sito)
        self.open_close_side_bar_btn.clicked.connect(self.slideMenu)
        self.notifiche_button.clicked.connect(self.vedi_notifiche)
        self.nome.setText(cliente.nome)
        self.logout_button.clicked.connect(self.logout)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()


    def logout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Sei sicuro di voler effettuare il logout?")
        msg.setStyleSheet("#customMessageBox { color: black; }")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            self.logout_requested = True
            self.login.clear_fields()
            self.login.show()
            self.close()


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

    def vedi_notifiche(self):
        self.VistaNotifiche=VistaNotifica(self.cliente,self.controller)
        self.VistaNotifiche.show()


    def open_sito(self):
        webbrowser.open(
            "https://www.tripadvisor.it/Restaurant_Review-g1934128-d15861838-Reviews-Il_Piccolo_Forno-Castelplanio_Province_of_Ancona_Marche.html")

    def update_time(self):
        time=datetime.now()
        formatted_time= time.strftime("%H:%M:%S")
        formatted_data=time.strftime("%d/%m/%Y")
        self.Ora.setText(formatted_time)
        self.Data.setText(formatted_data)

    def go_carrello(self,cliente):
        self.Carrello=VistaCarrello(cliente,self.controller,self.controllerp)
        self.Carrello.show()
    def go_Torte(self):
        self.Torte=PersonalizzaTorta(self.cliente)
        self.Torte.show()
    def go_Whishlist(self,cliente,controller):
        self.Whishlist=VistaWhishlist(cliente,controller)
        self.Whishlist.show()

    def go_Prodotti(self,cliente,controller):
        self.Shop=VistaListaProdotti(cliente,controller,self.controllerp)
        self.Shop.show()

    def closeEvent(self,event):
        if self.logout_requested:
            event.accept()
        else:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText("Sei sicuro di voler chiudere il programma?")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            result = msg.exec()

            if result == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()

