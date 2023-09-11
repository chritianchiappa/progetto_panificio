from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve,QDateTime
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from prodotto.controller.ControllerProdotto import ControllerProdotto
from cliente.controller.ControllerCliente import ControllerCliente
from ordine.model.Ordine import Ordine
from datetime import datetime
class VistaPagamento(QWidget):

    def __init__(self, prodotti,cliente,controllerp,controllerc,callback):
        super(VistaPagamento, self).__init__()
        uic.loadUi('ordine/view/VistaPagamento.ui', self)
        self.setWindowTitle("Check out")
        self.prodotti=prodotti
        self.cliente=cliente
        self.controller_lista_clienti=controllerc
        self.callback=callback
        self.controllerord = ControllerListaOrdini()
        self.controllerprodotti=controllerp
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

    def scala_quantita(self):
        for prodotto in self.prodotti:
            print(prodotto.nome)
            quantita_ord=ControllerProdotto(prodotto).get_quantita()
            prod_c=self.controllerprodotti.check_prodotto(prodotto.nome)
            quantita_prod=ControllerProdotto(prod_c).get_quantita()

            ControllerProdotto(prod_c).set_quantita(quantita_prod-quantita_ord)
            self.controllerprodotti.save_data()


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

    def verifica_quantita_disponibile(self):
        for prodotto in self.prodotti:
            quantita_ord = ControllerProdotto(prodotto).get_quantita()
            prod_c = self.controllerprodotti.check_prodotto(prodotto.nome)
            quantita_prod = ControllerProdotto(prod_c).get_quantita()

            if quantita_prod < quantita_ord:
                self.popup(f"Quantità insufficiente di {prodotto.nome} nel magazzino.", QMessageBox.Icon.Warning)
                return False

        return True

    def check_out(self):
        selected_datetime = self.time_edit_consegna.dateTime().toPyDateTime()
        if not self.verifica_quantita_disponibile():
            return
        elif self.ritiro_negozio.isChecked():
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
        self.scala_quantita()
        self.controllerord.inserisci_ordine(Ordine(
            self.prodotti,
            datetime.now(),
            self.cliente,
            indirizzo,
            data_consegna,
            False)
        )
        prodotti_da_rimuovere = self.prodotti[:]

        for prodotto_carrello in prodotti_da_rimuovere:
            print(prodotto_carrello.nome)
            ControllerCliente(self.cliente).rimuovi_prodotto_carrello(prodotto_carrello)
        self.controller_lista_clienti.save_data()
        self.controllerord.save_data()
        self.popup("Ordine effettuato con successo",QMessageBox.Icon.Information)
        self.callback()
        self.close()

    def popup(self,text,icon):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()


