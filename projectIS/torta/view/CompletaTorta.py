from PyQt6 import uic

from PyQt6.QtWidgets import QDialog,QMessageBox



class CompletaTorta(QDialog):

    def __init__(self,lista_ordini,ordine_selezionato,selected_row,torta):
        super(CompletaTorta, self).__init__()
        uic.loadUi('torta/view/CompletaTorta.ui', self)
        self.torta=torta
        self.lista_ordini=lista_ordini
        self.ordine_selezionato=ordine_selezionato
        self.selected_row=selected_row
        self.finisci_button.clicked.connect(self.termina_torta)




    def termina_torta(self):
        peso=self.selettore_peso.value()

        if peso!=0.0:
            prezzo = round(peso * 30, 2)
            self.torta.peso=peso
            self.torta.prezzo=prezzo

            self.lista_ordini.completa_salva_rimuovi(self.ordine_selezionato,self.selected_row,prezzo)
            self.close()
        else:
            self.pop_up()
    def pop_up(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Devi inserire un peso")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
