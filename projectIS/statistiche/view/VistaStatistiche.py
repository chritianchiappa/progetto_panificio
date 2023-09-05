from PyQt6 import uic
from PyQt6.QtWidgets import QWidget,QMessageBox,QHBoxLayout

from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from ordine.controller.ControllerOrdine import ControllerOrdine
from prodotto.controller.ControllerProdotto import ControllerProdotto
import numpy as np

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
        self.prodotti_piu_venduti_button.clicked.connect(self.mostra_grafico3)

    def mostra_grafico1(self):
        mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
        valori = [0] * len(mesi)  # Inizializza una lista di zeri per i valori

        for ordine in self.controllerlistord.get_lista_ordini():
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

        self.canvas.draw()


    def mostra_grafico2(self):
        distribuzione = {"Pane": 0,"Dolci": 0, "Biscotti": 0, "Pizze": 0}

        for ordine in self.controllerlistord.get_lista_ordini():
            for prodotto in ControllerOrdine(ordine).get_lista_prodotti_ordinati():

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

    def mostra_grafico3(self):
        mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
        prodotto_mensile = {}

        for mese in mesi:
            prodotto_mensile[mese] = {"prodotto": "", "quantita": 0, "incasso": 0}

        for ordine in self.controllerlistord.get_lista_ordini():
            mese_ordine = ControllerOrdine(ordine).get_mese_ordine()
            nome_mese = mesi[mese_ordine - 1]
            for prodotto in ControllerOrdine(ordine).get_lista_prodotti_ordinati():
                nome_prodotto = ControllerProdotto(prodotto).get_nome()
                quantita = ControllerProdotto(prodotto).get_quantita()
                incasso = ControllerProdotto(prodotto).get_prezzo()

                if quantita > prodotto_mensile[nome_mese]["quantita"]:
                    prodotto_mensile[nome_mese]["prodotto"] = nome_prodotto
                    prodotto_mensile[nome_mese]["quantita"] = quantita
                    prodotto_mensile[nome_mese]["incasso"] = incasso

        # Estrai dati per il grafico
        prodotti = [data["prodotto"] for data in prodotto_mensile.values()]
        incassi = [data["incasso"] for data in prodotto_mensile.values()]
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        x = range(len(mesi))
        larghezza_barre = 0.6

        bars = ax.bar(x, incassi, width=larghezza_barre, color='dodgerblue', alpha=0.7)

        ax.set_xlabel('Mesi')
        ax.set_ylabel('Incasso')
        ax.set_xticks([i for i in x])
        ax.set_xticklabels(mesi)

        for i, (bar, incasso, prodotto) in enumerate(zip(bars, incassi, prodotti)):
            ax.annotate(f"{prodotto}\n{quantita}", xy=(bar.get_x() + bar.get_width() / 2, quantita),
                        xytext=(0, 3),  # Sposta l'etichetta verso l'alto di 3 punti
                        textcoords='offset points',
                        ha='center', va='bottom')

        self.canvas.draw()














