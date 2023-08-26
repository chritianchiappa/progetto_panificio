from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from cliente.controller.ControllerCliente import ControllerCliente
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from ordine.model.Ordine import Ordine
from listaordini.controller.ListaOrdini import ControllerListaOrdini
from datetime import datetime
class VistaCarrello(QWidget):
     def __init__(self, cliente):
        super(VistaCarrello, self).__init__()
        uic.loadUi('carrello/view/vistaCarrello.ui', self)
        self.cliente=cliente
        self.controller = ControllerCliente(cliente)
        self.controllerprod = ControllerListaProdotti()
        self.controllerord = ControllerListaOrdini()
        self.update_ui()
        self.acquista_button.clicked.connect(self.acquista_selezionato)
        self.dettagli_button.clicked.connect(self.dettagli_selezionato)
        self.rimuovi_button.clicked.connect(self.rimuovi_selezionato)
        self.ordina_tutto_button.clicked.connect(self.ordina_tutto)

     def update_ui(self):
         self.listview_model = QStandardItemModel(self.list_view)

         for prodotto in self.controller.get_carrello_cliente():
             item = QStandardItem()
             item.setText(f"{prodotto.nome}  {prodotto.prezzo} €")
             item.setEditable(False)
             font = item.font()
             font.setPointSize(18)
             item.setFont(font)
             self.listview_model.appendRow(item)

         self.list_view.setModel(self.listview_model)
         self.prezzo_totale.setText(f"{self.controller.prezzo_totale_carrello} €")

     def acquista_selezionato(self):
         selected = self.list_view.selectedIndexes()[0].row()
         prodotto_selezionato = self.controller.get_prodotto_carrello_by_index(selected)
         self.controllerord.inserisci_ordine(Ordine(
             prodotto_selezionato,
             datetime.now(),
             prodotto_selezionato.get_prezzo(),
             self.cliente,
             False)
         )

     def dettagli_selezionato(self):
         selected = self.list_view.selectedIndexes()[0].row()
         prodotto_selezionato = self.cliente.carrello[selected]
         #collega il bottone con la seconda pag pag_2
         #setText delle label con i dettagli tipo allergeni ingredienti


     def rimuovi_selezionato(self):
         selected = self.list_view.selectedIndexes()
         if not selected:
            return
         selected_index = selected[0].row()
         self.cliente.carrello.pop(selected_index)
         #fai una funzione che elimina il prodotto in controllerCliente guarda controller dipendente
         self.listview_model.removeRow(selected_index)

     def ordina_tutto(self):
         #simile all acquisto

