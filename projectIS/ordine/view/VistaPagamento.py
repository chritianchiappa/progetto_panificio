from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve,QDateTime, QDate, QTime
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from prodotto.controller.ControllerProdotto import ControllerProdotto
from ordine.model.Ordine import Ordine
from datetime import datetime
class VistaPagamento(QWidget):

    def __init__(self, prodotti,cliente):
        super(VistaPagamento, self).__init__()
        uic.loadUi('ordine/view/VistaPagamento.ui', self)
        self.prodotti=prodotti
        self.cliente=cliente
        self.controllerord = ControllerListaOrdini()
        self.animation = QPropertyAnimation(self.slide_frame, b"maximumHeight")
        self.animation.setDuration(250)
        self.easing_curve = QEasingCurve(QEasingCurve.Type.Linear)
        self.indirizzo_consegna.setVisible(False)
        current_datetime = QDateTime.currentDateTime()
        self.time_edit_consegna.setDateTime(current_datetime)
        self.time_edit_consegna.setMinimumDateTime(current_datetime)
        self.prezzo_totale.setText(f"{self.calcola_importo()}")
        self.ritiro_negozio.toggled.connect(self.toggle_indirizzo_label)
        self.spedizione.toggled.connect(self.toggle_indirizzo_label)
        self.ordina_button.clicked.connect(self.check_out)


    def calcola_importo(self):
        importo=0
        for prodotto in self.prodotti:
            importo+=ControllerProdotto(prodotto).get_prezzo()
        return round(importo,2)



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
            self.prodotti,
            datetime.now(),
            self.cliente,
            indirizzo,
            data_consegna,
            False)
        )

        self.controllerord.save_data()
        self.popup("Ordine effettuato con successo",QMessageBox.Icon.Information)
        self.close()

    def popup(self,text,icon):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()


