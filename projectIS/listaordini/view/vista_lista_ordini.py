from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QTableWidgetItem,QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.controller.ControllerOrdine import ControllerOrdine
from torta.model.Torta import Torta
from torta.view.CompletaTorta import CompletaTorta


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
            self.tableWidget.setItem(row, 1, QTableWidgetItem(f"{ControllerOrdine(ordine).get_data_consegna()}"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{ControllerOrdine(ordine).get_indirizzo()}"))

            row+=1
    def mostra_dettagli(self):
        if self.dettagli_ordine_button.isChecked():
            torta_check=False
            selected_item = self.tableWidget.selectedItems()
            if not selected_item:
                self.dettagli_ordine_button.setChecked(False)
                return
            selected_row = selected_item[0].row()
            self.stackedWidget.setCurrentWidget(self.page_2)
            ordine_selezionato = self.controller.get_lista_ordini_non_completati()[selected_row]
            self.nome.setText(f"{ControllerOrdine(ordine_selezionato).get_nome_cliente()} {ControllerOrdine(ordine_selezionato).get_cognome_cliente()}")
            self.telefono.setText(f"{ControllerOrdine(ordine_selezionato).get_telefono_cliente()}")
            self.email.setText(f"{ControllerOrdine(ordine_selezionato).get_email_cliente()}")
            prodotti = ControllerOrdine(ordine_selezionato).get_lista_prodotti_ordinati()
            if isinstance(prodotti, Torta):
                self.titolo.setText("TORTA")
                torta_check=True
            else:
                self.titolo.setText("LISTA PRODOTTI")

            self.update_list(prodotti,torta_check)

        else:
            self.stackedWidget.setCurrentWidget(self.page_1)
    def update_list(self,prodotti,torta_check):
        self.listview_model = QStandardItemModel(self.list_view)

        if torta_check==True:
            base_item = QStandardItem()
            base_item.setText(f"Base: {prodotti.base}")
            base_item.setEditable(False)
            font = base_item.font()
            font.setPointSize(14)
            base_item.setFont(font)
            self.listview_model.appendRow(base_item)

            farcitura_item = QStandardItem()
            str_far=", ".join(farcitura for farcitura in prodotti.farciture)
            farcitura_item.setText(f"Farciture: {str_far}")
            farcitura_item.setEditable(False)
            font = farcitura_item.font()
            font.setPointSize(14)
            farcitura_item.setFont(font)
            self.listview_model.appendRow(farcitura_item)

            copertura_item = QStandardItem()
            copertura_item.setText(f"Copertura: {prodotti.copertura}")
            copertura_item.setEditable(False)
            font = copertura_item.font()
            font.setPointSize(14)
            copertura_item.setFont(font)
            self.listview_model.appendRow(copertura_item)

            richieste_item = QStandardItem()
            richieste_item.setText(f"Richieste: {prodotti.richieste}")
            richieste_item.setEditable(False)
            font = richieste_item.font()
            font.setPointSize(14)
            richieste_item.setFont(font)
            self.listview_model.appendRow(richieste_item)

        else:
            for prodotto in prodotti:
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
            prodotti_ordinati=ControllerOrdine(ordine_selezionato).get_lista_prodotti_ordinati()

            if isinstance(prodotti_ordinati,Torta):
                self.complTorta=CompletaTorta(self,ordine_selezionato,selected_row,prodotti_ordinati)
                self.complTorta.show()
            else:
                self.completa_salva_rimuovi(ordine_selezionato,selected_row)

    def completa_salva_rimuovi(self,ordine_selezionato,selected_row):
        ControllerOrdine(ordine_selezionato).completa_ordine()
        self.tableWidget.removeRow(selected_row)
        self.controller.save_data()







