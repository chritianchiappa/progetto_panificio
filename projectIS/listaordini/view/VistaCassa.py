from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from ordine.controller.ControllerOrdine import ControllerOrdine
from spesa.controller.ControllerSpesa import ControllerSpesa
from listaspese.controller.ControllerListaSpese import ControllerListaSpese
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini

from datetime import datetime
class VistaCassa(QWidget):

    def __init__(self):
        super(VistaCassa, self).__init__()
        uic.loadUi('listaordini/view/VistaCassa.ui', self)
        self.setWindowTitle("Cassa giornaliera")
        self.controllerspese=ControllerListaSpese()
        self.controllerord=ControllerListaOrdini()
        self.data_odierna=datetime.now()
        self.update_list_incassi()
        self.update_list_spese()
        self.incassi_button.clicked.connect(self.mostra_incassi)
        self.spese_button.clicked.connect(self.mostra_spese)
    def update_list_incassi(self):
        self.listview_model1 = QStandardItemModel(self.list_view)
        totale_incassi=0
        for ordine in self.controllerord.get_lista_ordini_completati():
            if ControllerOrdine(ordine).get_data().date()==self.data_odierna.date():
                totale_incassi += ControllerOrdine(ordine).get_importo()
                prodotti_ordinati=ControllerOrdine(ordine).get_lista_prodotti_ordinati()
                item = QStandardItem()
                if isinstance(prodotti_ordinati,list):
                    item.setText(f"Ordine di prodotti da {ControllerOrdine(ordine).get_nome_cliente()} {round(ControllerOrdine(ordine).get_importo(),2)}€")
                else:
                    item.setText(f"Ordine di torta da {ControllerOrdine(ordine).get_nome_cliente()} {round(ControllerOrdine(ordine).get_importo(),2)}€")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model1.appendRow(item)
        self.totale_incassi.setText(f"{round(totale_incassi, 2)}€")
        self.list_view.setModel(self.listview_model1)
    def update_list_spese(self):
        self.listview_model2 = QStandardItemModel(self.list_view1)
        totale_spese=0
        for spesa in self.controllerspese.get_lista_spese():
            if ControllerSpesa(spesa).get_data().date()==self.data_odierna.date():
                totale_spese+=ControllerSpesa(spesa).get_costo_ingrediente()
                item = QStandardItem()
                item.setText(f"Acquisto di {ControllerSpesa(spesa).get_nome_ingrediente()} {round(ControllerSpesa(spesa).get_costo_ingrediente(),2)}€")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model2.appendRow(item)
        self.totale_spese.setText(f"{round(totale_spese, 2)}€")
        self.list_view1.setModel(self.listview_model2)
    def mostra_incassi(self):
        self.label.setText("Incassi")
        self.stackedWidget.setCurrentWidget(self.page_1)


    def mostra_spese(self):
        self.label.setText("Spese")
        self.stackedWidget.setCurrentWidget(self.page_2)