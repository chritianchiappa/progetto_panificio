from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QLineEdit, QDialog,QMessageBox,QGraphicsDropShadowEffect
from PyQt6 import uic

from cliente.view.VistaRegisterUtente import VistaRegisterUtente
from dipendente.view.VistaRegisterDipendente import VistaRegisterDipendente
from amministratore.view.VistaLogAmm import VistaLogAmm

from dipendente.view.HomeDipendente import HomeDipendente
from cliente.view.HomeCliente import HomeCliente
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaingredienti.controller.controller_lista_ingredienti import ControllerListaIngredienti
from listadipendenti.controller.controller_lista_dipendenti import ControllerListaDipendenti

from risorse import res_rc

class VistaLogin(QDialog):
    def __init__(self,parent=None):
        super(VistaLogin, self).__init__(parent)
        uic.loadUi('login/view/vistalogin2.ui', self)
        self.setWindowTitle("Login")
        self.clear_fields()

        self.controllerprod=ControllerListaProdotti()
        self.controlleringr=ControllerListaIngredienti()
        self.controller=ControllerListaClienti()
        self.controllerdip=ControllerListaDipendenti()

        self.accedi_button.clicked.connect(self.go_Home)
        self.accedi_amm_button.clicked.connect(self.accedi_Amm)
        self.sel_registra.activated.connect(self.on_combobox_activated)
        self.sp_button.clicked.connect(self.show_password)

        shadow = QGraphicsDropShadowEffect() #serve per contornare i frame con delle ombre
        shadow.setColor(QColor(255, 255, 255, 100))  # Colore dell'ombra
        shadow.setBlurRadius(50)  # Raggio di sfocatura dell'ombra
        shadow.setOffset(0, 0)
        self.frame.setGraphicsEffect(shadow)
        self.frame_5.setGraphicsEffect(shadow)

    def clear_fields(self): #ripulisco tutti i campi del login per una successiva compilazione
        self.emailfield.clear()
        self.passwordfield.clear()
        self.error.clear()
        self.passwordfield.setEchoMode(QLineEdit.EchoMode.Password)
        self.sp_button.setChecked(False)




    def show_password(self): #mostra o nasconde la password in base allo stato del bottone
        if self.sp_button.isChecked():
            self.passwordfield.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordfield.setEchoMode(QLineEdit.EchoMode.Password)


    def on_combobox_activated(self, index): #seleziona una delle scelte della combobox
        selected_option = self.sel_registra.itemText(index)
        if selected_option=="Cliente":
            self.RegistraUtente = VistaRegisterUtente(self.controller)
            self.RegistraUtente.show()
        elif selected_option=="Dipendente":
            self.RegistraDipendente = VistaRegisterDipendente(self.controllerdip)
            self.RegistraDipendente.show()

    def go_Home(self):   #indirizza l utente(cliente/dipendente) in base all email e password nella rispettiva login
        email= self.emailfield.text()
        password= self.passwordfield.text()
        if len(email)==0 or len(password)==0:
            self.error.setText("alcuni campi non sono compilati")
            return
        utente_cliente = self.controller.check_cliente(email, password)
        utente_dipendente = self.controllerdip.check_dipendente(email, password)
        if utente_cliente:
            self.HomeC = HomeCliente(self,utente_cliente,self.controller,self.controllerprod)
            self.HomeC.show()
            self.hide()
        elif utente_dipendente:
            self.HomeD = HomeDipendente(self,utente_dipendente,self.controllerdip,self.controller,self.controllerprod,self.controlleringr)
            self.HomeD.show()
            self.hide()
        else:
            self.error.setText("email o password non corette")


    def accedi_Amm(self): #per la registrazione dell amministratore
        self.LogAmm= VistaLogAmm(self,self.controller,self.controllerdip)
        self.LogAmm.show()

    def closeEvent(self, event): #prima di chiudere la finestra del login invia un popup di conferma

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Sei sicuro di voler chiudere il programma?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
