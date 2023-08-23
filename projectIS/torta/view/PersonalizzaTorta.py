from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
class PersonalizzaTorta(QWidget):
    def __init__(self):
        super(PersonalizzaTorta,self).__init__()
        uic.loadUi('torta/view/Personalizza_torta.ui',self)
        self.base_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.farcitura_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.other_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))