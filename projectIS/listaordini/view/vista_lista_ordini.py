from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini

class VistaListaOrdini(QWidget):

    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)
        uic.loadUi('listaordini/view/vistaOrdini.ui', self)
        self.controller = ControllerListaOrdini()
        self.update_ui()
        first_index = self.listview_model.index(0, 0)
        self.list_view.setCurrentIndex(first_index)
        self.dettagli_ordine_button.clicked.connect(self.mostra_dettagli)
        self.completato_button.clicked.connect(self.completa_ordine)

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