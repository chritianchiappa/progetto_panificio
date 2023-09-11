from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from ordine.view.RiepilogoTorta import RiepilogoTorta
from torta.model.Torta import Torta
class PersonalizzaTorta(QWidget):
    def __init__(self,cliente):
        super(PersonalizzaTorta,self).__init__()
        uic.loadUi('torta/view/Personalizza_torta.ui',self)
        self.setWindowTitle("Personalizzazione torta")
        self.cliente=cliente

        self.current_page = self.stackedWidget.currentIndex()
        self.avanti_button.setEnabled(False)

        self.selected_page2 = None

        self.avanti_button.clicked.connect(self.nextPage)
        self.indietro_button.clicked.connect(self.prevPage)
        self.ordina_button.clicked.connect(self.ordina_torta)
        self.pandispagna.toggled.connect(self.checkRadioButton)
        self.pasta_biscuit.toggled.connect(self.checkRadioButton)
        self.pasta_frolla.toggled.connect(self.checkRadioButton)
        self.pasta_bigne.toggled.connect(self.checkRadioButton)
        self.pasta_sfoglia.toggled.connect(self.checkRadioButton)
        self.crema_pasticcera.toggled.connect(self.checkCheckbox),
        self.crema_chantilly.toggled.connect(self.checkCheckbox),
        self.marmellate.toggled.connect(self.checkCheckbox),
        self.crema_pistacchio.toggled.connect(self.checkCheckbox),
        self.crema_cioccolato.toggled.connect(self.checkCheckbox),
        self.crema_nocciola.toggled.connect(self.checkCheckbox),
        self.crema_caffe.toggled.connect(self.checkCheckbox),
        self.crema_ciocc_mandorla.toggled.connect(self.checkCheckbox),
        self.crema_ciocc_bianco.toggled.connect(self.checkCheckbox),
        self.crema_semifreddi_mousse.toggled.connect(self.checkCheckbox),
        self.frutta.toggled.connect(self.checkCheckbox)
        self.panna_montata.toggled.connect(self.checkRadioButton2)
        self.glasse_frutta.toggled.connect(self.checkRadioButton2)
        self.cioccolato_ganache.toggled.connect(self.checkRadioButton2)
        self.mousse_creme.toggled.connect(self.checkRadioButton2)
        self.pasta_zucchero.toggled.connect(self.checkRadioButton2)
        self.selezione_pagina_1 = None
        self.selezione_pagina_2 = []
        self.selezione_pagina_3 = None
        self.updateProgressBar()

    def checkRadioButton(self):
        if self.pandispagna.isChecked():
            self.selezione_pagina_1 = self.pandispagna.text()
        elif self.pasta_biscuit.isChecked():
            self.selezione_pagina_1 = self.pasta_biscuit.text()
        elif self.pasta_frolla.isChecked():
            self.selezione_pagina_1 = self.pasta_frolla.text()
        elif self.pasta_bigne.isChecked():
            self.selezione_pagina_1 = self.pasta_bigne.text()
        elif self.pasta_sfoglia.isChecked():
            self.selezione_pagina_1 = self.pasta_sfoglia.text()
        else:
            self.selezione_pagina_1 = None
        # Abilita il pulsante "Avanti" se almeno un radio button è selezionato
        if self.selezione_pagina_1:
            self.selected_page1=True

            self.avanti_button.setEnabled(True)
        else:
            self.avanti_button.setEnabled(False)

    def checkCheckbox(self):
        # Abilita il pulsante "Avanti" solo se almeno una checkbox è selezionata
        num_checked = sum([
            self.crema_pasticcera.isChecked(),
            self.crema_chantilly.isChecked(),
            self.marmellate.isChecked(),
            self.crema_pistacchio.isChecked(),
            self.crema_cioccolato.isChecked(),
            self.crema_nocciola.isChecked(),
            self.crema_caffe.isChecked(),
            self.crema_ciocc_mandorla.isChecked(),
            self.crema_ciocc_bianco.isChecked(),
            self.crema_semifreddi_mousse.isChecked(),
            self.frutta.isChecked()
        ])

        if num_checked >= 1 and num_checked <= 2:
            self.selected_page2=True
            self.avanti_button.setEnabled(True)
        else:
            self.avanti_button.setEnabled(False)

    def checkRadioButton2(self):

        if self.panna_montata.isChecked():
            self.selezione_pagina_3 = self.panna_montata.text()
        elif self.glasse_frutta.isChecked():
            self.selezione_pagina_3 = self.glasse_frutta.text()
        elif self.cioccolato_ganache.isChecked():
            self.selezione_pagina_3 = self.cioccolato_ganache.text()
        elif self.mousse_creme.isChecked():
            self.selezione_pagina_3 = self.mousse_creme.text()
        elif self.pasta_zucchero.isChecked():
            self.selezione_pagina_3 = self.pasta_zucchero.text()
        else:
            self.selezione_pagina_3 = None
        if self.selezione_pagina_3:

            self.avanti_button.setEnabled(True)
        else:
            self.avanti_button.setEnabled(False)

    def prevPage(self):

        if self.current_page> 0:
            self.current_page -= 1
            self.stackedWidget.setCurrentIndex(self.current_page)
            self.updateProgressBar()
            self.avanti_button.setEnabled(True)

    def nextPage(self):
        if self.current_page < self.stackedWidget.count() - 1:

            if self.current_page==0 and self.selected_page2==True:
                self.avanti_button.setEnabled(True)
            elif self.current_page==1 and self.selezione_pagina_3:
                self.avanti_button.setEnabled(True)
            else:
                self.avanti_button.setEnabled(False)

            self.current_page += 1
            self.stackedWidget.setCurrentIndex(self.current_page)
            self.updateProgressBar()


    def updateProgressBar(self):
        progress_value = int((self.current_page * 100) / (self.stackedWidget.count() - 1))
        self.progressBar.setValue(progress_value)

    def ordina_torta(self):

        checkbox_selezionate = [
            self.crema_pasticcera,
            self.crema_chantilly,
            self.marmellate,
            self.crema_pistacchio,
            self.crema_cioccolato,
            self.crema_nocciola,
            self.crema_caffe,
            self.crema_ciocc_mandorla,
            self.crema_ciocc_bianco,
            self.crema_semifreddi_mousse,
            self.frutta
        ]
        self.selezione_pagina_2 = [checkbox.text() for checkbox in checkbox_selezionate if checkbox.isChecked()]
        ulteriori_richieste = self.richieste.text().strip()
        torta=Torta(self.selezione_pagina_1,self.selezione_pagina_2,self.selezione_pagina_3,ulteriori_richieste,None,None)
        self.ComplOrd=RiepilogoTorta(torta,self.cliente,self)
        self.ComplOrd.show()




