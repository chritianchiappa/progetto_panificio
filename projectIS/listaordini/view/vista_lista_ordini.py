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
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setRowCount(len(self.controller.get_lista_ordini()))
        row=0
        for ordine in self.controller.get_lista_ordini():
            str_nome=ordine.cliente.nome+ordine.cliente.cognome
            print(str_nome)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str_nome))
            self.tableWidget.setItem(row,1,QTableWidgetItem(f"{ordine.data}"))
            row+=1
    def mostra_dettagli(self):
        print("dettagli")

    def completa_ordine(self):
        print("completato")
