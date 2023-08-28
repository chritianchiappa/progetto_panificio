from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QLineEdit, QDialog,QMessageBox,QGraphicsDropShadowEffect
from PyQt6 import uic

from home.view.VistaRegisterUtente import VistaRegisterUtente
from home.view.VistaRegisterDipendente import VistaRegisterDipendente
from home.view.VistaLogAmm import VistaLogAmm
from utilizzatore.view.HomeAmministratore import HomeAmministratore
from utilizzatore.view.HomeDipendente import HomeDipendente
from cliente.view.HomeCliente import HomeCliente
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listaclienti.model.lista_clienti import ListaClienti
from listadipendenti.controller.controller_lista_dipendenti import ControllerListaDipendenti
from listadipendenti.model.lista_dipendenti import ListaDipendenti

from home.view import res_rc

class VistaLogin(QDialog):
    def __init__(self,parent=None):
        super(VistaLogin, self).__init__(parent)
        uic.loadUi('home/view/vistalogin2.ui', self)
        self.setWindowTitle("Login")
        self.controller=ControllerListaClienti()
        self.controllerdip=ControllerListaDipendenti()
        self.accedi_button.clicked.connect(self.go_Home)
        self.accedi_amm_button.clicked.connect(self.accedi_Amm)
        self.sel_registra.activated.connect(self.on_combobox_activated)
        self.sp_button.clicked.connect(self.show_password)
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(255, 255, 255, 100))  # Colore dell'ombra
        shadow.setBlurRadius(50)  # Raggio di sfocatura dell'ombra
        shadow.setOffset(0, 0)
        self.frame.setGraphicsEffect(shadow)
        self.frame_5.setGraphicsEffect(shadow)


    def show_password(self):
        if self.sp_button.isChecked():
            self.passwordfield.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordfield.setEchoMode(QLineEdit.EchoMode.Password)


    def on_combobox_activated(self, index):
        selected_option = self.sel_registra.itemText(index)
        if selected_option=="Utente":
            self.RegistraUtente = VistaRegisterUtente(self.controller)
            self.RegistraUtente.show()
        elif selected_option=="Dipendente":
            self.RegistraDipendente = VistaRegisterDipendente(self.controllerdip)
            self.RegistraDipendente.show()

    def show_login(self):
        self.show()

    def go_Home(self):
        email= self.emailfield.text()
        password= self.passwordfield.text()
        if len(email)==0 or len(password)==0:
            self.error.setText("alcuni campi non sono compilati")
            return
        utente_cliente = self.controller.check_cliente(email, password)
        utente_dipendente = self.controllerdip.check_dipendente(email, password)
        if utente_cliente:
            self.HomeC = HomeCliente(self,utente_cliente)
            self.HomeC.show()
        elif utente_dipendente:
            self.HomeD = HomeDipendente(self,utente_dipendente)
            self.HomeD.show()
        else:
            self.error.setText("email o password non corette")


    def accedi_Amm(self):
        self.LogAmm= VistaLogAmm(self,HomeAmministratore())
        self.LogAmm.show()

    def closeEvent(self, event):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Sei sicuro di voler chiudere il programma?")
        msg.setStyleSheet('color: white; '
                          )
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
