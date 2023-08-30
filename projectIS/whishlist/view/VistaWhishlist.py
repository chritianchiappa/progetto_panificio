from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from cliente.controller.ControllerCliente import ControllerCliente


class VistaWhishlist(QWidget):
    def __init__(self, cliente,controller):
        super(VistaWhishlist, self).__init__()
        uic.loadUi('whishlist/view/vistaWhishlist.ui', self)
        self.cliente = cliente
        self.controller_lista_clienti = controller
        self.controller = ControllerCliente(cliente)
        self.update_ui()
        first_index = self.listview_model.index(0, 0)
        self.list_view.setCurrentIndex(first_index)
        self.rimuovi_button.clicked.connect(self.rimuovi_selezionato)


    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in self.controller.get_whishlist_cliente():
            item = QStandardItem()
            item.setText(f"{prodotto.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)

    def rimuovi_selezionato(self):
        selected = self.list_view.selectedIndexes()
        if not selected:
            return
        selected_index = selected[0].row()
        self.controller.rimuovi_prodotto_whishlist_index(selected_index)
        self.listview_model.removeRow(selected_index)

    def closeEvent(self, event):
        self.controller_lista_clienti.aggiorna_whishlist_cliente(self.cliente.email, self.cliente.password,
                                                                self.cliente.whishlist)
        self.controller_lista_clienti.save_data()
