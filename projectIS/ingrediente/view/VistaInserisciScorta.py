from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
from PyQt6.QtCore import QDateTime
from ingrediente.model.Ingrediente import Ingrediente
from listaspese.controller.ControllerListaSpese import ControllerListaSpese
from spesa.model.Spesa import Spesa
from datetime import datetime

class VistaInserisciScorta(QWidget):
    def __init__(self,magazzino,controller_ingredienti):
        super(VistaInserisciScorta, self).__init__()
        uic.loadUi('ingrediente/view/VistaInserisciScorta.ui', self)
        self.setWindowTitle("Inserisci scorta")
        self.controlleringr = controller_ingredienti
        self.controllerspese=ControllerListaSpese()
        self.magazzino=magazzino
        current_datetime = QDateTime.currentDateTime()
        self.data_scadenza.setDateTime(current_datetime)
        self.data_scadenza.setMinimumDateTime(current_datetime)
        self.new_scorta_button.clicked.connect(self.aggiungi_scorta)

    def aggiungi_scorta(self):
        nome=self.nome.text().strip()
        prezzo = self.prezzo.value()
        quantita=self.quantita.value()
        allergeni=self.allergeni.text().strip()
        unita_misura=self.selettore_unita.currentText()
        lista_allergeni = allergeni.split(',')
        selected_date = self.data_scadenza.dateTime().toPyDateTime().date()

        if unita_misura.strip() == "":
            self.popup("Seleziona un unita di misura", QMessageBox.Icon.Warning, QMessageBox.StandardButton.Ok)
            return

        elif len(nome)==0:
            self.popup("Inserisci il nome della scorta",QMessageBox.Icon.Warning,QMessageBox.StandardButton.Ok)
            return

        else:
            ingrediente=Ingrediente(
                nome,
                prezzo,
                unita_misura,
                quantita,
                lista_allergeni,
                selected_date)

            self.controlleringr.inserisci_ingrediente(ingrediente)
            self.controllerspese.inserisci_spesa(Spesa(
                ingrediente,
                datetime.now()

            ))
            self.popup("ingrediente aggiunto all elenco", QMessageBox.Icon.Information, QMessageBox.StandardButton.Ok)
            self.close()
            self.magazzino.update_list_scorte()
            self.controlleringr.save_data()
            self.controllerspese.save_data()


    def popup(self,text,icon,button):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setStandardButtons(button)
        msg.setDefaultButton(button)
        msg.exec()