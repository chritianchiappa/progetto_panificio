from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from ordine.view.VistaPagamento import VistaPagamento
class PersonalizzaTorta(QWidget):
    def __init__(self):
        super(PersonalizzaTorta,self).__init__()
        uic.loadUi('torta/view/Personalizza_torta.ui',self)
        self.base_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.farcitura_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.copertura_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.other_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.ordina_button.clicked.connect(self.ordina_torta)

    def ordina_torta(self):
        self.ComplOrd=VistaPagamento()
        self.ComplOrd.show()




