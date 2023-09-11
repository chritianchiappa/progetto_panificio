from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve,QDateTime
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.model.Ordine import Ordine
from datetime import datetime
class RiepilogoTorta(QWidget):
    def __init__(self,torta,cliente,PersTorta):
        super(RiepilogoTorta,self).__init__()
        uic.loadUi('ordine/view/RiepilogoTorta.ui',self)
        self.setWindowTitle("Riepilogo torta")
        self.torta=torta
        self.PersTorta=PersTorta
        self.cliente=cliente
        self.controllerord = ControllerListaOrdini()
        self.animation = QPropertyAnimation(self.slide_frame, b"maximumHeight")
        self.animation.setDuration(250)
        self.easing_curve = QEasingCurve(QEasingCurve.Type.Linear)
        self.indirizzo_consegna.setVisible(False)
        self.update_campi()


        current_datetime = QDateTime.currentDateTime()
        self.time_edit_consegna.setDateTime(current_datetime)
        self.time_edit_consegna.setMinimumDateTime(current_datetime)
        self.ritiro_negozio.toggled.connect(self.toggle_indirizzo_label)
        self.spedizione.toggled.connect(self.toggle_indirizzo_label)
        self.ordina_button.clicked.connect(self.check_out)

    def update_campi(self):
        self.base.setText(self.torta.base)
        str_farc = ", ".join(farcitura for farcitura in self.torta.farciture)
        self.farcitura.setText(str_farc)
        self.copertura.setText(self.torta.copertura)
        self.richieste.setText(self.torta.richieste)


    def toggle_indirizzo_label(self):
        if self.spedizione.isChecked():
            self.animation.setStartValue(0)
            self.animation.setEndValue(60)
            self.indirizzo_consegna.setVisible(True)
        else:
            self.animation.setStartValue(self.slide_frame.sizeHint().height())
            self.animation.setEndValue(0)
            self.indirizzo_consegna.setVisible(False)


        self.animation.setEasingCurve(self.easing_curve)
        self.animation.start()
    def check_out(self):
        selected_datetime = self.time_edit_consegna.dateTime().toPyDateTime()

        if self.ritiro_negozio.isChecked():
            str_indirizzo = "Negozio"
        elif self.spedizione.isChecked():
            str_indirizzo = self.indirizzo_consegna.text().strip()
            if len(str_indirizzo) == 0:
                self.popup("Inserisci un indirizzo di consegna valido",QMessageBox.Icon.Warning)
                return

        else:
            self.popup("Seleziona una procedura per l'ordine",QMessageBox.Icon.Warning)
            return

        self.ordina(str_indirizzo,selected_datetime)
    def ordina(self,indirizzo,data_consegna):
        self.controllerord.inserisci_ordine(Ordine(
            self.torta,
            datetime.now(),
            self.cliente,
            indirizzo,
            data_consegna,
            False)
        )

        self.controllerord.save_data()
        self.popup("Ordine effettuato con successo",QMessageBox.Icon.Information)
        self.close()
        self.PersTorta.close()

    def popup(self,text,icon):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()