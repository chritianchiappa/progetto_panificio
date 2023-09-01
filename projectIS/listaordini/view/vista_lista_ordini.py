from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QTableWidgetItem
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.controller.ControllerOrdine import ControllerOrdine


class VistaListaOrdini(QWidget):

    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)
        uic.loadUi('listaordini/view/vistaOrdini.ui', self)
        self.controller = ControllerListaOrdini()

        self.update_ui()
        self.dettagli_ordine_button.clicked.connect(self.mostra_dettagli)
        self.completato_button.clicked.connect(self.completa_ordine)

    def update_ui(self):
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setRowCount(len(self.controller.get_lista_ordini_non_completati()))
        row=0
        for ordine in self.controller.get_lista_ordini_non_completati():
            self.tableWidget.setItem(row, 0, QTableWidgetItem(f"{ControllerOrdine(ordine).get_nome_cliente()} {ControllerOrdine(ordine).get_cognome_cliente()}"))
            self.tableWidget.setItem(row,1,QTableWidgetItem(f"{ControllerOrdine(ordine).get_data_ordine()}"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{ControllerOrdine(ordine).get_indirizzo()}"))
            row+=1
    def mostra_dettagli(self):
        print("dettagli")

    def completa_ordine(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:  # Verifica se una riga è stata selezionata
            ordine_selezionato = self.controller.get_lista_ordini_non_completati()[selected_row]
            ControllerOrdine(ordine_selezionato).completa_ordine()
            self.tableWidget.removeRow(selected_row)
            self.controller.save_data()

