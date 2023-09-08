from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listadipendenti.view.vista_inserisci_dipendente import VistaInserisciDipendente

from dipendente.view.vista_dipendente import VistaDipendente
class VistaListaDipendenti(QWidget):

    def __init__(self,controllerdip):
        super(VistaListaDipendenti, self).__init__()
        uic.loadUi('listadipendenti/view/vistalistadipendenti.ui', self)
        self.controller = controllerdip
        self.update_ui()
        first_index = self.listview_model.index(0, 0)
        self.list_view.setCurrentIndex(first_index)
        self.new_button.clicked.connect(self.show_new_dipendente)
        self.open_button.clicked.connect(self.mostra_selezionato)
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

    def mostra_selezionato(self):
        selected = self.list_view.selectedIndexes()[0].row()
        dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
        self.vista_dipendente = VistaDipendente(dipendente_selezionato)
        self.vista_dipendente.show()

    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller,self.update_ui)
        self.vista_inserisci_dipendente.show()

    def elimina_selezionato(self):
        selected = self.list_view.selectedIndexes()
        if not selected:
            return
        selected_index=selected[0].row()
        self.controller.rimuovi_dipendente_by_index(selected_index)
        self.controller.save_data()
        self.listview_model.removeRow(selected_index)








