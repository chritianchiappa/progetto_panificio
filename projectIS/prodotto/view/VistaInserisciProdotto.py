from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from prodotto.model.Prodotto import Prodotto
from listaingredienti.controller.controller_lista_ingredienti import ControllerListaIngredienti


class VistaInserisciProdotto(QWidget):
    def __init__(self,controller_prodotti):
        super(VistaInserisciProdotto, self).__init__()
        uic.loadUi('prodotto/view/VistaInserisciProdotto.ui', self)
        self.controllerprod = controller_prodotti
        self.new_prodotto_button.clicked.connect(self.aggiungi_prodotto)
        self.pixmap = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            pixmap = QPixmap(file_path)
            pixmap_scaled = pixmap.scaled(320, 220, Qt.AspectRatioMode.KeepAspectRatio)
            self.label_immagine.setPixmap(pixmap_scaled)
            event.accept()
            self.pixmap = pixmap
        else:
            print("non accetto")



    def aggiungi_prodotto(self):
        nome=self.nome.text().strip()
        quantita=self.quantita.text().strip()
        tipo=self.tipo.currentText()
        prezzo=self.prezzo.text().strip()
        ingredienti=self.ingredienti.text()
        if tipo.strip() == "":
            self.popup("Seleziona un tipo di prodotto", QMessageBox.Icon.Warning, QMessageBox.StandardButton.Ok)
            return  # Interrompi il processo se non è stato selezionato un tipo

        elif len(nome)==0 or len(quantita)==0 or len(prezzo)==0 or len(ingredienti)==0:
            self.popup("Alcuni campi non sono compilati",QMessageBox.Icon.Warning,QMessageBox.StandardButton.Ok)
            return
        elif self.pixmap is None:
            self.popup("Carica un'immagine", QMessageBox.Icon.Warning, QMessageBox.StandardButton.Ok)
            return
        else:
            output_folder = "immagini"
            output_file = os.path.join(output_folder, nome + ".png")
            self.pixmap.save(output_file)

            lista_ingredienti=[]
            lista_nomi_ingredienti = ingredienti.split(',')
            for ingrediente_nome in lista_nomi_ingredienti:
                ingrediente_corrispondente = None
                for ingrediente_obj in ControllerListaIngredienti().get_lista_ingredienti():
                    if ingrediente_obj.nome == ingrediente_nome:
                        ingrediente_corrispondente = ingrediente_obj
                        break  # Esci dal ciclo una volta trovato il corrispondente
                if ingrediente_corrispondente:
                    lista_ingredienti.append(ingrediente_corrispondente)
                else:
                    self.popup(f"Ingrediente non trovato: {ingrediente_nome}", QMessageBox.Icon.Warning, QMessageBox.StandardButton.Ok)
                    return

            self.controllerprod.inserisci_prodotto(Prodotto(
                nome,
                tipo,
                prezzo,
                lista_ingredienti,
                quantita
            ))
            self.controllerprod.save_data()

    def popup(self,text,icon,button):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setStandardButtons(button)
        msg.setDefaultButton(button)
        msg.exec()



