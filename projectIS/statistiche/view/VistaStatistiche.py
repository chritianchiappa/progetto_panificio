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
        anno_corrente = datetime.datetime.now().year
        for anno in range(2020, anno_corrente + 1):
            self.selettore_anno.addItem(str(anno))
        self.selettore_anno.activated.connect(self.update_graph)
        self.grafico_attuale = None
        self.anno_selezionato=anno_corrente
        self.mostra_grafico1()
        self.vendite_mensili_button.clicked.connect(self.mostra_grafico1)
        self.vendite_tipologia_button.clicked.connect(self.mostra_grafico2)
        self.prodotti_piu_venduti_button.clicked.connect(self.mostra_grafico3)
        self.stats_torte_button.clicked.connect(self.mostra_grafico4)
        self.stats_clienti_button.clicked.connect(self.mostra_grafico5)
        self.stats_consegna_button.clicked.connect(self.mostra_grafico6)

    def update_graph(self):

        self.anno_selezionato = int(self.selettore_anno.currentText())

        # Controlla quale tipo di grafico era visualizzato prima del cambiamento
        if self.grafico_attuale == "G1":
            self.mostra_grafico1()
        elif self.grafico_attuale == "G2":
            self.mostra_grafico2()
        elif self.grafico_attuale == "G3":
            self.mostra_grafico3()
        elif self.grafico_attuale == "G4":
            self.mostra_grafico4()
        elif self.grafico_attuale == "G5":
            self.mostra_grafico5()
        elif self.grafico_attuale == "G6":
            self.mostra_grafico6()


    def mostra_grafico1(self):
        self.grafico_attuale="G1"
        mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
        valori = [0] * len(mesi)  # Inizializza una lista di zeri per i valori

        for ordine in self.controllerlistord.get_lista_ordini_completati():
            if ControllerOrdine(ordine).get_anno_ordine()==self.anno_selezionato:
                mese_ordine = ControllerOrdine(ordine).get_mese_ordine()
                valori[mese_ordine - 1] += ControllerOrdine(ordine).get_importo()


        # Crea il grafico a barre
        self.figure.clear()  # Cancella qualsiasi grafico precedente dal canvas
        ax = self.figure.add_subplot(111)

        ax.plot(mesi, valori, marker='o', linestyle='none', color='#F29B00',linewidth=2)
        ax.set_xlabel('Mesi')
        ax.set_ylabel('Vendite (€)')
        ax.set_title('Vendite Mensili')
        ax.grid(True)  # Aggiungi una griglia al grafico

        for i, txt in enumerate(valori):
            ax.annotate(round(txt,2), (mesi[i], valori[i]), textcoords="offset points", xytext=(0, 10), ha='center')

        self.canvas.draw()


    def mostra_grafico2(self):
        self.grafico_attuale="G2"
        distribuzione = {"Pane": 0,"Dolci": 0, "Biscotti": 0, "Pizze": 0}

        for ordine in self.controllerlistord.get_lista_ordini_completati():
            if ControllerOrdine(ordine).get_anno_ordine()==self.anno_selezionato:
                prodotti_ordinati = ControllerOrdine(ordine).get_lista_prodotti_ordinati()
                if isinstance(prodotti_ordinati,list):
                    for prodotto in prodotti_ordinati:
                        if ControllerProdotto(prodotto).get_tipo() in distribuzione:
                            distribuzione[ControllerProdotto(prodotto).get_tipo()]+=1

        # Creare il grafico a torta
        labels = list(distribuzione.keys())
        sizes = list(distribuzione.values())

        if any(sizes):
            explode = [0.05, 0.05, 0.05, 0.05]
            colors = plt.get_cmap('YlOrBr')(np.linspace(0.2, 0.7, len(sizes)))
            self.figure.clear()  # Cancella qualsiasi grafico precedente dal canvas

            ax = self.figure.add_subplot(111)

            ax.pie(sizes, labels=labels,
                   wedgeprops={"linewidth": 1, "edgecolor": "black"}, autopct='%1.1f%%', startangle=90, explode=explode,
                   colors=colors)

            ax.axis('equal')

        else:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.text(0.5, 0.5, 'Nessun dato disponibile', ha='center', va='center', fontsize=12)

        self.canvas.draw()



    def mostra_grafico3(self):
        self.grafico_attuale = "G3"
        mesi = {"gen": {"conteggi": {}}, "feb": {"conteggi": {}}, "mar": {"conteggi": {}}, "apr": {"conteggi": {}},
                "mag": {"conteggi": {}}, "giu": {"conteggi": {}}, "lug": {"conteggi": {}}, "ago": {"conteggi": {}},
                "set": {"conteggi": {}}, "ott": {"conteggi": {}}, "nov": {"conteggi": {}}, "dic": {"conteggi": {}}}

        mesiNum = {1: "gen", 2: "feb", 3: "mar", 4: "apr", 5: "mag", 6: "giu", 7: "lug", 8: "ago", 9: "set", 10: "ott",
                   11: "nov", 12: "dic"}
        dati_tabella = [["Mese", "Prodotto", "Quantità"]]

        for ordine in self.controllerlistord.get_lista_ordini():
            for mese, mesiNome in zip(mesiNum, mesi):
                if mese == ControllerOrdine(ordine).get_mese_ordine():
                    for prod in ControllerOrdine(ordine).get_lista_prodotti_ordinati():
                        if ControllerProdotto(prod).get_nome() in mesi[mesiNome]["conteggi"]:
                            mesi[mesiNome]["conteggi"][ControllerProdotto(prod).get_nome()] += ControllerProdotto(
                                prod).get_quantita()
                        else:
                            mesi[mesiNome]["conteggi"][ControllerProdotto(prod).get_nome()] = ControllerProdotto(
                                prod).get_quantita()

        for mesiNome in mesi:
            prodotti_ordinati = sorted(mesi[mesiNome]["conteggi"].items(), key=lambda x: x[1], reverse=True)
            primo_prodotto = dict(prodotti_ordinati[:1])
            nome = list(primo_prodotto.keys())
            quantita = list(primo_prodotto.values())
            dati_tabella.append([mesiNome, nome, quantita])

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        tabella = ax.table(cellText=dati_tabella, loc='center', cellLoc='center')

        ax.axis('off')

        tabella.auto_set_font_size(False)
        tabella.set_fontsize(12)
        tabella.scale(1.2, 1.2)
        self.canvas.draw()
    def mostra_grafico4(self):
        self.grafico_attuale = "G4"
        categorie_base = Counter()
        categorie_farcitura = Counter()
        categorie_copertura = Counter()
        for ordine in self.controllerlistord.get_lista_ordini_completati():
            if ControllerOrdine(ordine).get_anno_ordine()==self.anno_selezionato:
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
    def mostra_grafico5(self):
        self.grafico_attuale = "G5"
        clienti_ordini = {}
        clienti_spese ={}
        for ordine in self.controllerlistord.get_lista_ordini_completati():
            if ControllerOrdine(ordine).get_anno_ordine() == self.anno_selezionato:

                nome_cliente = ControllerOrdine(ordine).get_nome_cliente()
                email_cliente = ControllerOrdine(ordine).get_email_cliente()

            # Usare la combinazione di nome ed email come chiave per identificare univocamente i clienti
                chiave_cliente = (nome_cliente, email_cliente)

                if chiave_cliente in clienti_ordini:
                    clienti_ordini[chiave_cliente] += 1
                else:
                    clienti_ordini[chiave_cliente] = 1
                if chiave_cliente in clienti_spese:
                    clienti_spese[chiave_cliente] += ControllerOrdine(ordine).get_importo()
                else:
                    clienti_spese[chiave_cliente] = ControllerOrdine(ordine).get_importo()

        clienti_ordini_ordinati = dict(sorted(clienti_ordini.items(), key=lambda item: item[1], reverse=True))
        clienti_spese_ordinati = dict(sorted(clienti_spese.items(), key=lambda item: item[1], reverse=True))
        # Estrai i nomi dei clienti e il numero di ordini in liste separate
        nomi_clienti1 = [cliente[0] for cliente in clienti_ordini_ordinati.keys()]
        nomi_clienti2 = [cliente[0] for cliente in clienti_spese_ordinati.keys()]
        num_ordini = list(clienti_ordini_ordinati.values())
        spese = list(clienti_spese_ordinati.values())
        email_clienti1 = [cliente[1] for cliente in clienti_ordini_ordinati.keys()]
        email_clienti2 = [cliente[1] for cliente in clienti_spese_ordinati.keys()]

        # Seleziona solo i primi 5 clienti con più ordini
        num_clienti_da_mostrare = 5
        nomi_clienti_da_mostrare = nomi_clienti1[:num_clienti_da_mostrare]
        nomi_clienti_da_mostrare2 = nomi_clienti2[:num_clienti_da_mostrare]
        num_ordini_da_mostrare = num_ordini[:num_clienti_da_mostrare]
        spese_da_mostrare = spese[:num_clienti_da_mostrare]
        clienti_email_da_mostrare = email_clienti1[:num_clienti_da_mostrare]
        clienti_email_da_mostrare2 = email_clienti2[:num_clienti_da_mostrare]

        self.figure.clear()
        self.figure.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        ax1 = self.figure.add_subplot(211)
        ax2 = self.figure.add_subplot(212)
        ax2.axis('tight')
        ax2.axis('off')

        ax1.axis('tight')
        ax1.axis('off')

        dati_tabella1 = []
        dati_tabella2 = []

        for i in range(num_clienti_da_mostrare):
            if i < len(nomi_clienti_da_mostrare) and i < len(num_ordini_da_mostrare):
                # Aggiungi i dati del cliente (nome, email) e il numero di ordini alla tabella
                dati_tabella1.append(
                    [nomi_clienti_da_mostrare[i], clienti_email_da_mostrare[i], num_ordini_da_mostrare[i]])
            else:
                # Gestisci il caso in cui non ci sono abbastanza elementi nella lista
                dati_tabella1.append(["N/A", "N/A", "N/A"])
        for i in range(num_clienti_da_mostrare):
            if i < len(nomi_clienti_da_mostrare2) and i < len(spese_da_mostrare):
                # Aggiungi i dati del cliente (nome, email) e il numero di ordini alla tabella
                dati_tabella2.append(
                    [nomi_clienti_da_mostrare2[i], clienti_email_da_mostrare2[i], spese_da_mostrare[i]])
            else:
                # Gestisci il caso in cui non ci sono abbastanza elementi nella lista
                dati_tabella2.append(["N/A", "N/A", "N/A"])

        tabella = ax1.table(cellText=dati_tabella1, colLabels=["Cliente", "Email","Numero di Ordini"],loc='upper left',
                           cellLoc='center',bbox=[0.1,0.5,0.8,0.6])
        tabella2 = ax2.table(cellText=dati_tabella2, colLabels=["Cliente", "Email", "Spese"],loc='lower left',
                            cellLoc='center',bbox=[0.1,0.0,0.8,0.6])
        tabella.auto_set_font_size(False)
        tabella.set_fontsize(12)
        tabella.scale(1.5, 1.5)
        tabella2.auto_set_font_size(False)
        tabella2.set_fontsize(12)
        tabella2.scale(1.5, 1.5)

        self.canvas.draw()

    def mostra_grafico6(self):
        self.grafico_attuale = "G6"
        categorie_ordini = Counter()
        for ordine in self.controllerlistord.get_lista_ordini_completati():
            if ControllerOrdine(ordine).get_anno_ordine() == self.anno_selezionato:
                if ControllerOrdine(ordine).get_indirizzo()=="Negozio":
                    categorie_ordini["Ritiro in negozio"] += 1
                else:
                    categorie_ordini["Consegna a domicilio"] += 1
        categorie = list(categorie_ordini.keys())
        num_ordini = list(categorie_ordini.values())

        if any(num_ordini):
            self.figure.clear()  # Cancella qualsiasi grafico precedente dal canvas

            ax = self.figure.add_subplot(111)
            ax.bar(categorie, num_ordini, width=0.4, color=['#F29B00', '#a36902'])
            ax.set_ylabel('Numero di ordini')
            ax.set_xticks(np.arange(len(categorie)))
            ax.set_xticklabels(categorie)
        else:
            # Se non ci sono dati, cancella completamente il grafico e mostra solo il messaggio
            self.figure.clf()  # Cancella completamente il grafico
            ax = self.figure.add_subplot(111)
            ax.text(0.5, 0.5, 'Nessun dato disponibile', ha='center', va='center', fontsize=12)

        self.canvas.draw()



























