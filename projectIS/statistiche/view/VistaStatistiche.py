from collections import Counter

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox,QHBoxLayout

from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.controller.ControllerOrdine import ControllerOrdine
from prodotto.controller.ControllerProdotto import ControllerProdotto
import numpy as np
import datetime
from torta.model.Torta import Torta


class VistaStatistiche(QWidget):
    def __init__(self):
        super(VistaStatistiche, self).__init__()
        uic.loadUi('statistiche/view/VistaStatistiche.ui', self)
        plt.style.use('classic')
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.horizontaLayout = QHBoxLayout(self.frame_plot)
        self.horizontaLayout.addWidget(self.canvas)
        self.controllerlistord=ControllerListaOrdini()
        self.mostra_grafico1()
        self.vendite_mensili_button.clicked.connect(self.mostra_grafico1)
        self.vendite_tipologia_button.clicked.connect(self.mostra_grafico2)
        #self.prodotti_piu_venduti_button.clicked.connect(self.mostra_grafico3)
        self.stats_torte_button.clicked.connect(self.mostra_grafico4)


    def mostra_grafico1(self):
        mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
        valori = [0] * len(mesi)  # Inizializza una lista di zeri per i valori

        for ordine in self.controllerlistord.get_lista_ordini_completati():
            mese_ordine = ControllerOrdine(ordine).get_mese_ordine() # Ottieni il mese dell'ordine
            valori[mese_ordine - 1] += ControllerOrdine(ordine).get_importo()


        # Crea il grafico a barre
        self.figure.clear()  # Cancella qualsiasi grafico precedente dal canvas
        ax = self.figure.add_subplot(111)

        ax.plot(mesi, valori, marker='o', linestyle='-', color='#F29B00',linewidth=2)
        ax.set_xlabel('Mesi')
        ax.set_ylabel('Vendite')
        ax.set_title('Vendite Mensili')
        ax.grid(True)  # Aggiungi una griglia al grafico

        '''cursor = mplcursors.cursor(hover=True)

        def formatta_etichetta(sel):
            # mese_selezionato = mesi[sel.target.index]
            vendita_corrispondente = valori[sel.target.index]
            sel.annotation.set_text(f'Vendite: {vendita_corrispondente}')

        cursor.connect("add", formatta_etichetta)'''

        self.canvas.draw()


    def mostra_grafico2(self):
        distribuzione = {"Pane": 0,"Dolci": 0, "Biscotti": 0, "Pizze": 0}

        for ordine in self.controllerlistord.get_lista_ordini_completati():
            prodotti_ordinati = ControllerOrdine(ordine).get_lista_prodotti_ordinati()
            if isinstance(prodotti_ordinati,list):
                for prodotto in prodotti_ordinati:
                    if ControllerProdotto(prodotto).get_tipo() in distribuzione:
                        distribuzione[ControllerProdotto(prodotto).get_tipo()]+=1

        # Creare il grafico a torta
        labels = list(distribuzione.keys())
        sizes = list(distribuzione.values())
        explode=[0.05,0.05,0.05,0.05]
        colors = plt.get_cmap('YlOrBr')(np.linspace(0.2, 0.7, len(sizes)))
        self.figure.clear()  # Cancella qualsiasi grafico precedente dal canvas

        ax = self.figure.add_subplot(111)

        ax.pie(sizes, labels=labels,
        wedgeprops = {"linewidth": 1, "edgecolor": "black"}, autopct='%1.1f%%', startangle=90,explode=explode,colors=colors)

        ax.axis('equal')  # Equal aspect ratio per un grafico circolare

        # Aggiorna il canvas per mostrare il nuovo grafico
        self.canvas.draw()

    '''def mostra_grafico3(self):
        conteggi = {}

        for ordine in self.controllerlistord.get_lista_ordini():
            print(ordine)
            for prod in ControllerOrdine(ordine).get_lista_prodotti_ordinati():
                print(prod)
                if ControllerProdotto(prod).get_nome() in conteggi:
                    conteggi[ControllerProdotto(prod).get_nome()] += ControllerProdotto(prod).get_quantita()
                else:
                    conteggi[ControllerProdotto(prod).get_nome()] = ControllerProdotto(prod).get_quantita()

        print(conteggi)

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        tabella = ax.table(cellText=dati, loc='center', cellLoc='center')

        ax.axis('off')

        tabella.auto_set_font_size(False)
        tabella.set_fontsize(12)
        tabella.scale(1.2, 1.2)

        self.canvas.draw()'''
    def mostra_grafico4(self):
        categorie_base = Counter()
        categorie_farcitura = Counter()
        categorie_copertura = Counter()
        for ordine in self.controllerlistord.get_lista_ordini_completati():
            prodotti_ordinati = ControllerOrdine(ordine).get_lista_prodotti_ordinati()
            if isinstance(prodotti_ordinati,Torta):
                base = prodotti_ordinati.base
                farcitura = prodotti_ordinati.farciture
                copertura = prodotti_ordinati.copertura

                categorie_base[base] += 1
                categorie_farcitura.update(farcitura)
                categorie_copertura[copertura] += 1

        categorie_b = list(categorie_base.keys())
        quantita_b = list(categorie_base.values())
        categorie_f = list(categorie_farcitura.keys())
        quantita_f = list(categorie_farcitura.values())
        categorie_c = list(categorie_copertura.keys())
        quantita_c = list(categorie_copertura.values())

        self.figure.clear()

        colors_b = plt.get_cmap('Oranges')(np.linspace(0.2, 0.7, len(categorie_b)))
        colors_f= plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(categorie_f)))
        colors_c = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(categorie_c)))
        ax1 = self.figure.add_subplot(311)
        explode_b = [0.1] * len(categorie_b)
        ax1.pie(quantita_b, labels=categorie_b, autopct='%1.1f%%',wedgeprops = {"linewidth": 1, "edgecolor": "black"},startangle=90,explode=explode_b,colors=colors_b)
        ax1.set_title("Base")

        ax2 = self.figure.add_subplot(312)
        explode_f = [0.1] * len(categorie_f)
        ax2.pie(quantita_f, labels=categorie_f, autopct='%1.1f%%',wedgeprops = {"linewidth": 1, "edgecolor": "black"},startangle=90,explode=explode_f,colors=colors_f)
        ax2.set_title("Farcitura")

        ax3 = self.figure.add_subplot(313)
        explode_c = [0.1] * len(categorie_c)
        ax3.pie(quantita_c, labels=categorie_c, autopct='%1.1f%%',wedgeprops = {"linewidth": 1, "edgecolor": "black"},startangle=90,explode=explode_c,colors=colors_c)
        ax3.set_title("Copertura")

        plt.subplots_adjust(hspace=0.5)
        self.canvas.draw()




















