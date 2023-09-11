from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from cliente.controller.ControllerCliente import ControllerCliente
from dipendente.controller.controller_dipendente import ControllerDipendente
from cliente.model.Cliente import Cliente



class VistaNotifica(QWidget):
    def __init__(self,utente,controller):
        super(VistaNotifica,self).__init__()
        uic.loadUi('notifica/view/VistaNotifica.ui',self)
        self.setWindowTitle("Notifiche")
        self.utente=utente

        if isinstance(self.utente, Cliente):
            self.controller_lista = controller
            self.controller = ControllerCliente(self.utente)
        else:
            self.controller_lista = controller
            self.controller = ControllerDipendente(self.utente)
        self.update_ui()
        first_index = self.listview_model.index(0, 0)
        self.list_view.setCurrentIndex(first_index)
        self.dettagli_notifica_button.clicked.connect(self.dettagli_messaggio)
        self.rimuovi_notifica_button.clicked.connect(self.rimuovi_notifica)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)

        for notifica in self.controller.get_lista_notifiche():
            item = QStandardItem()
            item.setText(f"{notifica.titolo} ")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)

        self.list_view.setModel(self.listview_model)

    def dettagli_messaggio(self):
        if self.dettagli_notifica_button.isChecked():
            selected_index = self.list_view.selectedIndexes()
            if not selected_index:  # Verifica se la lista è vuota o nessun elemento selezionato
                self.dettagli_notifica_button.setChecked(False)
                return

            selected_row = selected_index[0].row()
            if selected_row < 0:  # Verifica se l'indice è valido
                return
            self.stackedWidget.setCurrentWidget(self.page_2)
            notifica_selezionata= self.controller.get_notifica_by_index(selected_row)
            self.messaggio.setText(notifica_selezionata.messaggio)
            self.messaggio.setWordWrap(True)
        else:
            self.stackedWidget.setCurrentWidget(self.page_1)

    def rimuovi_notifica(self):
        selected = self.list_view.selectedIndexes()
        if not selected:
            return
        selected_index = selected[0].row()
        self.controller.rimuovi_notifica_by_index(selected_index)
        self.listview_model.removeRow(selected_index)
        if self.stackedWidget.currentWidget() == self.page_2:
            self.stackedWidget.setCurrentWidget(self.page_1)
            self.dettagli_notifica_button.setChecked(False)
        self.update_ui()

    def closeEvent(self, event):
        self.controller_lista.save_data()