from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaingredienti.controller.controller_lista_ingredienti import ControllerListaIngredienti
from prodotto.controller.ControllerProdotto import ControllerProdotto
from prodotto.view.VistaModificaQuantita import VistaModificaQuantita
from prodotto.view.VistaInserisciProdotto import VistaInserisciProdotto
from ingrediente.view.VistaInserisciScorta import VistaInserisciScorta


class VistaMagazzino(QWidget):
    def __init__(self):
        super(VistaMagazzino, self).__init__()
        uic.loadUi('listaprodotti/view/VistaMagazzino.ui', self)
        self.controllerprod = ControllerListaProdotti()
        self.controlleringr = ControllerListaIngredienti()
        self.update_list_prodotti()
        self.update_list_scorte()
        first_index1 = self.listview_model1.index(0, 0)
        self.list_view1.setCurrentIndex(first_index1)
        first_index2 = self.listview_model2.index(0, 0)
        self.list_view2.setCurrentIndex(first_index2)
        self.prodotti_button.clicked.connect(self.show_prodotti)
        self.scorte_button.clicked.connect(self.show_scorte)
        self.mod_quantita1_button.clicked.connect(self.mod_quantita_prodotto)
        self.agg_prod_button.clicked.connect(self.agg_prodotto)
        self.rim_prod_button.clicked.connect(self.rim_prodotto)
        self.rim_scorta_button.clicked.connect(self.rim_scorta)
        self.mod_quantita2_button.clicked.connect(self.mod_quantita_scorta)
        self.agg_scorta_button.clicked.connect(self.agg_scorta)


    def update_list_prodotti(self):
        self.listview_model1 = QStandardItemModel(self.list_view1)
        for prodotto in self.controllerprod.get_lista_prodotti():
            item = QStandardItem()
            if prodotto.quantita==0:
                quantita="esaurito"
            else:
                quantita=str(prodotto.quantita)+ "pz"
            item.setText(f"{prodotto.nome}  {quantita}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model1.appendRow(item)

        self.list_view1.setModel(self.listview_model1)

    def update_list_scorte(self):
        self.listview_model2 = QStandardItemModel(self.list_view2)
        for ingrediente in self.controlleringr.get_lista_ingredienti():
            item = QStandardItem()
            if ingrediente.quantita == 0:
                quantita = "esaurito"
            else:
                quantita = str(ingrediente.quantita) + ingrediente.unita_misura
            item.setText(f"{ingrediente.nome}  {quantita}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model2.appendRow(item)

        self.list_view2.setModel(self.listview_model2)


    def show_prodotti(self):
        self.label.setText("Prodotti")
        self.stackedWidget.setCurrentWidget(self.page_1)


    def show_scorte(self):
        self.label.setText("Scorte")
        self.stackedWidget.setCurrentWidget(self.page_2)

    def mod_quantita_prodotto(self):
        selected_indexes = self.list_view1.selectedIndexes()
        if not selected_indexes:  # Verifica se la lista è vuota o nessun elemento selezionato
            return

        selected_row = selected_indexes[0].row()
        if selected_row < 0:  # Verifica se l'indice è valido
            return
        prodotto_selezionato = self.controllerprod.get_prodotto_by_index(selected_row)
        self.ModQuantita=VistaModificaQuantita(self,prodotto_selezionato,self.controllerprod)
        self.ModQuantita.show()

    def mod_quantita_scorta(self):
        print("mod quantita")

    def agg_prodotto(self):
        self.InsertProd=VistaInserisciProdotto(self.controllerprod)
        self.InsertProd.show()

    def agg_scorta(self):
        self.InsertScorta=VistaInserisciScorta(self,self.controlleringr)
        self.InsertScorta.show()

    def rim_prodotto(self):
        selected_index = self.list_view1.selectedIndexes()
        if not selected_index:  # Verifica se la lista è vuota o nessun elemento selezionato
            return

        selected_row = selected_index[0].row()
        if selected_row < 0:  # Verifica se l'indice è valido
            return
        self.controllerprod.rimuovi_prodotto_by_index(selected_row)
        self.listview_model1.removeRow(selected_row)

    def rim_scorta(self):
        selected_index = self.list_view2.selectedIndexes()
        if not selected_index:  # Verifica se la lista è vuota o nessun elemento selezionato
            return

        selected_row = selected_index[0].row()
        if selected_row < 0:  # Verifica se l'indice è valido
            return
        self.controlleringr.rimuovi_ingrediente_by_index(selected_row)
        self.listview_model2.removeRow(selected_row)






