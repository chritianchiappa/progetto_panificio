from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listadipendenti.view.vista_inserisci_dipendente import VistaInserisciDipendente
from dipendente.controller.controller_dipendente import ControllerDipendente

class VistaListaDipendenti(QWidget):

    def __init__(self,controllerdip):
        super(VistaListaDipendenti, self).__init__()
        uic.loadUi('listadipendenti/view/vistalistadipendenti.ui', self)
        self.setWindowTitle("Lista dipendenti")
        self.controller = controllerdip
        self.update_ui()
        first_index = self.listview_model.index(0, 0)
        self.list_view.setCurrentIndex(first_index)
        self.new_button.clicked.connect(self.show_new_dipendente)
        self.dettagli_button.clicked.connect(self.dettagli_selezionato)
        self.delete_button.clicked.connect(self.elimina_selezionato)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(f"{dipendente.cognome} {dipendente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller,self.update_ui)
        self.vista_inserisci_dipendente.show()

    def dettagli_selezionato(self):
        if self.dettagli_button.isChecked():
            selected_indexes = self.list_view.selectedIndexes()
            if not selected_indexes:  # Verifica se la lista è vuota o nessun elemento selezionato
                self.dettagli_button.setChecked(False)
                return

            selected_row = selected_indexes[0].row()
            if selected_row < 0:  # Verifica se l'indice è valido
                return
            self.stackedWidget.setCurrentWidget(self.page_2)
            dipendente_selezionato = self.controller.get_dipendente_by_index(selected_row)
            self.nome_cognome_label.setText(
                f"{ControllerDipendente(dipendente_selezionato).get_nome_dipendente()} {ControllerDipendente(dipendente_selezionato).get_cognome_dipendente()}")
            self.id_label.setText(f"{ControllerDipendente(dipendente_selezionato).get_id_dipendente()}")
            self.indirizzo_label.setText(f"{ControllerDipendente(dipendente_selezionato).get_indirizzo_dipendente()}")
            self.cfiscale_label.setText(f"{ControllerDipendente(dipendente_selezionato).get_cfiscale_dipendente()}")
            self.telefono_label.setText(f"{ControllerDipendente(dipendente_selezionato).get_telefono_dipendente()}")
        else:
            self.stackedWidget.setCurrentWidget(self.page_1)


    def elimina_selezionato(self):
        selected = self.list_view.selectedIndexes()
        if not selected:
            return
        selected_index=selected[0].row()
        self.controller.rimuovi_dipendente_by_index(selected_index)
        self.listview_model.removeRow(selected_index)
        if self.stackedWidget.currentWidget() == self.page_2:
            self.stackedWidget.setCurrentWidget(self.page_1)
            self.dettagli_button.setChecked(False)
        self.controller.save_data()
        self.update_ui()








