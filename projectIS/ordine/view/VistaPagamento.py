from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.model.Ordine import Ordine
from datetime import datetime
class VistaPagamento(QWidget):

    def __init__(self, prodotti,cliente):
        super(VistaPagamento, self).__init__()
        uic.loadUi('ordine/view/VistaPagamento.ui', self)
        self.prodotti=prodotti
        self.cliente=cliente
        self.controllerord = ControllerListaOrdini()
        self.ordina_button.clicked.connect(self.check_out)

    def check_out(self):
        self.animation = QPropertyAnimation(self.slide_frame, b"maximumHeight")
        self.animation.setDuration(250)
        easing_curve = QEasingCurve(QEasingCurve.Type.Linear)
        str_indirizzo=""
        if self.ritiro_negozio.isChecked():
            str_indirizzo="negozio"
            self.ordina(str_indirizzo)

        elif self.spedizione.isChecked():
            self.animation.setStartValue(0)
            self.animation.setEndValue(100)
            self.animation.setEasingCurve(easing_curve)
            self.animation.start()
            if len(self.indirizzo_consegna.text())==0:
                self.popup_errore("immetti un indirizzo di consegna")
            else:
                str_indirizzo=self.indirizzo_consegna.text()
                self.ordina(str_indirizzo)
        else:
            self.popup_errore("seleziona una procedura per l' ordine")


    def ordina(self,indirizzo):
        self.controllerord.inserisci_ordine(Ordine(
            self.prodotti,
            datetime.now(),
            self.cliente,
            indirizzo,
            False)
        )

        self.controllerord.save_data()

    def popup_errore(self,text):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()


