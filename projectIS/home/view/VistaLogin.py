
from PyQt6.QtWidgets import QLineEdit, QDialog, QGraphicsView, QGraphicsScene
from PyQt6 import uic
from home.view.VistaHome import VistaHome
from home.view.VistaRegisterUtente import VistaRegisterUtente
from home.view.VistaRegisterDipendente import VistaRegisterDipendente
from home.view.VistaLogAmm import VistaLogAmm
from utilizzatore.view.HomeAmministratore import HomeAmministratore
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listaclienti.model.lista_clienti import ListaClienti
from listadipendenti.controller.controller_lista_dipendenti import ControllerListaDipendenti
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
        elif selected_option=="dipendente":
            self.RegistraDipendente = VistaRegisterDipendente(self.controllerdip)
            self.RegistraDipendente.show()

    def show_login(self):
        self.show()

    def go_Home(self):
        lista_clienti = ListaClienti()
        email= self.emailfield.text()
        password= self.passwordfield.text()
        if len(email)==0 or len(password)==0:
            self.error.setText("alcuni campi non sono compilati")
        else:
            t = False
            print(lista_clienti.get_lista_clienti())
            for cliente in lista_clienti.get_lista_clienti():
                if cliente.check_cliente(email,password)==True:
                    print("ciao!: "+ cliente.nome)
                    t=True
                    break
            if t==False:
                self.error.setText("nessun utente trovato, registrati")


    def accedi_Amm(self):
        self.LogAmm= VistaLogAmm(self,HomeAmministratore())
        self.LogAmm.show()
