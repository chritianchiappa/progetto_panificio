from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QTableWidgetItem,QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
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
        if self.dettagli_ordine_button.isChecked():
            selected_item = self.tableWidget.selectedItems()
            if selected_item:
                selected_row = selected_item[0].row()
                self.stackedWidget.setCurrentWidget(self.page_2)
                ordine_selezionato = self.controller.get_lista_ordini_non_completati()[selected_row]
                self.nome.setText(f"{ControllerOrdine(ordine_selezionato).get_nome_cliente()} {ControllerOrdine(ordine_selezionato).get_cognome_cliente()}")
                self.telefono.setText(f"{ControllerOrdine(ordine_selezionato).get_telefono_cliente()}")
                self.email.setText(f"{ControllerOrdine(ordine_selezionato).get_email_cliente()}")
                self.update_list(ordine_selezionato)
        else:
            self.stackedWidget.setCurrentWidget(self.page_1)
    def update_list(self,ordine):
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in ControllerOrdine(ordine).get_lista_prodotti_ordinati():
            item = QStandardItem()
            item.setText(f"{prodotto.nome}  {prodotto.quantita} pz")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)



    def completa_ordine(self):
        selected_item = self.tableWidget.selectedItems()
        if selected_item:
            selected_row = selected_item[0].row()  # Ottieni l'indice della riga selezionata
            ordine_selezionato = self.controller.get_lista_ordini_non_completati()[selected_row]
            ControllerOrdine(ordine_selezionato).completa_ordine()
            self.tableWidget.removeRow(selected_row)
            self.controller.save_data()


