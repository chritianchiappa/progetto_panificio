from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from cliente.controller.ControllerCliente import ControllerCliente


from ordine.view.VistaPagamento import VistaPagamento

from prodotto.controller.ControllerProdotto import ControllerProdotto


class VistaCarrello(QWidget):
     def __init__(self, cliente,controller,controllerp):
        super(VistaCarrello, self).__init__()
        uic.loadUi('carrello/view/vistaCarrello.ui', self)
        self.cliente=cliente
        self.controller = ControllerCliente(cliente)
        self.controllerprodotti = controllerp

        self.controller_lista_clienti = controller
        self.update_ui()
        first_index = self.listview_model.index(0, 0)
        self.list_view.setCurrentIndex(first_index)
        self.acquista_button.clicked.connect(self.acquista_selezionato)
        self.dettagli_button.clicked.connect(self.dettagli_selezionato)
        self.rimuovi_button.clicked.connect(self.rimuovi_selezionato)
        self.ordina_tutto_button.clicked.connect(self.ordina_tutto)

     def update_ui(self):
         self.listview_model = QStandardItemModel(self.list_view)
         for prodotto in self.controller.get_carrello_cliente():
             item = QStandardItem()
             item.setText(f"{prodotto.nome}  {prodotto.quantita} pz")
             item.setEditable(False)
             font = item.font()
             font.setPointSize(18)
             item.setFont(font)
             self.listview_model.appendRow(item)

         self.list_view.setModel(self.listview_model)
         importo=self.controller.prezzo_totale_carrello()
         self.prezzo_totale.setText(f"{round(importo,2)} €")

     def acquista_selezionato(self):
         selected_index = self.list_view.selectedIndexes()
         if not selected_index:  # Verifica se la lista è vuota o nessun elemento selezionato
             return
         selected_row = selected_index[0].row()
         if selected_row < 0:  # Verifica se l'indice è valido
             return
         prodotto_selezionato = self.controller.get_prodotto_carrello_by_index(selected)
         self.VistaOrdFin = VistaPagamento([prodotto_selezionato],self.cliente,self.controllerprodotti,self.controller_lista_clienti,self.update_ui)
         self.VistaOrdFin.show()


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
             prodotto_selezionato = self.cliente.carrello[selected_row]
             self.nome.setText(ControllerProdotto(prodotto_selezionato).get_nome())
             self.prezzo.setText(f"{round(ControllerProdotto(prodotto_selezionato).get_prezzo(),2)}")
             str_ingr = ", ".join(ingrediente.nome for ingrediente in ControllerProdotto(prodotto_selezionato).get_lista_ingredienti())
             self.ingredienti.setText(str_ingr)
             str_all = ", ".join(allergene for allergene in ControllerProdotto(prodotto_selezionato).get_allergeni())
             self.allergeni.setText(str_all)
         else:
             self.stackedWidget.setCurrentWidget(self.page_1)


     def rimuovi_selezionato(self):
         selected = self.list_view.selectedIndexes()
         if not selected:
            return
         selected_index = selected[0].row()
         self.controller.rimuovi_prodotto_carrello_index(selected_index)
         self.listview_model.removeRow(selected_index)
         self.update_ui()

     def ordina_tutto(self):
         self.VistaOrdFin = VistaPagamento(self.controller.get_carrello_cliente(), self.cliente,self.controllerprodotti,self.controller_lista_clienti,self.update_ui)
         self.VistaOrdFin.show()


     def closeEvent(self, event):
         #self.controller_lista_clienti.aggiorna_carrello_cliente(self.cliente.email, self.cliente.password,
                                                                 #self.cliente.carrello)
         self.controller_lista_clienti.save_data()



