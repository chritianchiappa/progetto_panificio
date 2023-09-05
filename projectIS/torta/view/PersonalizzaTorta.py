from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from ordine.view.VistaPagamento import VistaPagamento
class PersonalizzaTorta(QWidget):
    def __init__(self):
        super(PersonalizzaTorta,self).__init__()
        uic.loadUi('torta/view/Personalizza_torta.ui',self)
        self.current_page = self.stackedWidget.currentIndex()
        self.avanti_button.setEnabled(False)
        self.avanti_button.clicked.connect(self.nextPage)
        self.indietro_button.clicked.connect(self.prevPage)
        self.ordina_button.clicked.connect(self.ordina_torta)
        self.pandispagna.toggled.connect(self.checkRadioButton)
        self.pasta_biscuit.toggled.connect(self.checkRadioButton)
        self.pasta_frolla.toggled.connect(self.checkRadioButton)
        self.pasta_bigne.toggled.connect(self.checkRadioButton)
        self.pasta_sfoglia.toggled.connect(self.checkRadioButton)
        self.updateProgressBar()

    def checkRadioButton(self):
        # Abilita il pulsante "Avanti" se almeno un radio button è selezionato
        if self.pandispagna.isChecked() or self.pasta_biscuit.isChecked() or self.pasta_frolla.isChecked() or self.pasta_bigne.isChecked() or self.pasta_sfoglia.isChecked():
            self.avanti_button.setEnabled(True)
        else:
            self.avanti_button.setEnabled(False)

    def prevPage(self):

        if self.current_page> 0:
            self.current_page -= 1
            self.stackedWidget.setCurrentIndex(self.current_page)
            self.updateProgressBar()

    def nextPage(self):

        if self.current_page < self.stackedWidget.count() - 1:
            self.current_page += 1
            self.stackedWidget.setCurrentIndex(self.current_page)
            self.updateProgressBar()

    def updateProgressBar(self):
        progress_value = int((self.current_page * 100) / (self.stackedWidget.count() - 1))
        self.progressBar.setValue(progress_value)

    def ordina_torta(self):
        self.ComplOrd=VistaPagamento()
        self.ComplOrd.show()




