from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox
import os
import shutil
from prodotto.model.Prodotto import Prodotto
from listaingredienti.controller.controller_lista_ingredienti import ControllerListaIngredienti


class VistaInserisciProdotto(QWidget):
    def __init__(self,controller_prodotti):
        super(VistaInserisciProdotto, self).__init__()
        uic.loadUi('prodotto/view/VistaInserisciProdotto.ui', self)
        self.controllerprod = controller_prodotti
        self.new_prodotto_button.clicked.connect(self.aggiungi_prodotto)

    def sposta_file(self,percorso_file, cartella_destinazione,nome_prodotto):
        try:
            if os.path.exists(percorso_file):
                if not os.path.exists(cartella_destinazione):
                    os.makedirs(cartella_destinazione)

                percorso_destinazione = os.path.join(cartella_destinazione, nome_prodotto)

                shutil.move(percorso_file, percorso_destinazione)


            else:
                print(f"Il percorso del file '{percorso_file}' non esiste.")

        except Exception as e:
            print(f"Si è verificato un errore durante lo spostamento del file: {str(e)}")



    def aggiungi_prodotto(self):
        nome=self.nome.text().strip()
        quantita=self.quantita.text().strip()
        tipo=self.tipo.currentText()
        prezzo=self.prezzo.text().strip()
        ingredienti=self.ingredienti.text()
        url_immagine= self.url_immagine.text()
        if tipo.strip() == "":
            self.popup("Seleziona un tipo di prodotto", QMessageBox.Icon.Warning, QMessageBox.StandardButton.Ok)
            return  # Interrompi il processo se non è stato selezionato un tipo

        elif len(nome)==0 or len(quantita)==0 or len(prezzo)==0 or len(ingredienti)==0:
            self.popup("Alcuni campi non sono compilati",QMessageBox.Icon.Warning,QMessageBox.StandardButton.Ok)
            return

        else:
            self.sposta_file(url_immagine,"immagini/",nome)
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
            self.popup("prodotto aggiunto all elenco",QMessageBox.Icon.Information,QMessageBox.StandardButton.Ok)
            self.controllerprod.save_data()

    def popup(self,text,icon,button):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setStandardButtons(button)
        msg.setDefaultButton(button)
        msg.exec()



