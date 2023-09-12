from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve
from notifica.model.Notifica import Notifica

from PyQt6 import uic

from cliente.controller.ControllerCliente import ControllerCliente

from dipendente.controller.controller_dipendente import ControllerDipendente


class InviaNotifica(QWidget):
    def __init__(self,controller,controllerdip):
        super(InviaNotifica,self).__init__()
        uic.loadUi('notifica/view/InviaNotifica.ui',self)
        self.setWindowTitle("Invia notifica")
        self.controllerc=controller
        self.controllerd = controllerdip
        self.animation = QPropertyAnimation(self.slide_frame, b"maximumHeight")
        self.animation.setDuration(250)
        self.easing_curve = QEasingCurve(QEasingCurve.Type.Linear)
        self.n_p_dipendente.toggled.connect(self.toggle_id_label)
        self.id_label.setVisible(False)
        self.invia_button.clicked.connect(self.invia_notifica)

    def toggle_id_label(self):
        if self.n_p_dipendente.isChecked():
            self.animation.setStartValue(0)
            self.animation.setEndValue(60)
            self.id_label.setVisible(True)
        else:
            self.animation.setStartValue(self.slide_frame.sizeHint().height())
            self.animation.setEndValue(0)
            self.id_label.setVisible(False)


        self.animation.setEasingCurve(self.easing_curve)
        self.animation.start()

    def invia_notifica(self):
        titolo=self.titolo.text().strip()
        messaggio = self.messaggio.text().strip()
        if len(titolo)==0:
            self.popup("immetti un titolo ", QMessageBox.Icon.Warning)
            return
        elif len(messaggio)==0:
            self.popup("immetti un messaggio ", QMessageBox.Icon.Warning)
            return
        elif self.n_clienti.isChecked():
            for cliente in self.controllerc.get_lista_clienti():
                ControllerCliente(cliente).aggiungi_notifica(Notifica(titolo,messaggio))
            self.controllerc.save_data()
        elif self.n_dipendenti.isChecked():
            for dipendente in self.controllerd.get_lista_dipendenti():
                ControllerDipendente(dipendente).aggiungi_notifica(Notifica(titolo,messaggio))
            self.controllerd.save_data()
        elif self.n_p_dipendente.isChecked():
            id=self.id_label.text().strip()
            if len(id) == 0:
                self.popup("Inserisci un id",QMessageBox.Icon.Warning)
                return
            else:
                dipendente=self.controllerd.check_dipendente_by_id(id)
                if dipendente:
                    ControllerDipendente(dipendente).aggiungi_notifica(Notifica(titolo, messaggio))
                    self.controllerd.save_data()
                else:
                    self.popup("Dipendente non esistente, prova ad inserire un id valido", QMessageBox.Icon.Warning)
                    return

        else:
            self.popup("Seleziona un destinatario",QMessageBox.Icon.Warning)
            return
        self.popup("Messaggio inviato con successo", QMessageBox.Icon.Information)
        self.close()



    def popup(self,text,icon):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()


