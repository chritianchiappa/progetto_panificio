import unittest
from ordine.controller.ControllerOrdine import ControllerOrdine
from cliente.model.Cliente import Cliente
from torta.model.Torta import Torta
from ordine.model.Ordine import Ordine
from ingrediente.model.Ingrediente import Ingrediente
from prodotto.model.Prodotto import Prodotto
from datetime import datetime

#Faccio dei test sulla classe ControllerOrdine
class TestOrdine(unittest.TestCase):
    def setUp(self): #inizializzo tutti i dati che mi serviranno per i test
        data_consegna = datetime(2023, 9, 23, 15, 30)
        self.ingrediente1 = Ingrediente("farina 00", 1.24, 10, "Kg", ["glutine"], "31-12-2023")
        self.ingrediente2 = Ingrediente("uova", 0.50, 10, "Pz", ["uova"], "31-12-2023")
        self.prodotto1 = Prodotto("Ciambellone",
                                  "Dolci",
                                  16.00,
                                  [self.ingrediente1, self.ingrediente2],
                                  1)
        self.prodotto2 = Prodotto("Brioche",
                                  "Dolci",
                                  1.20,
                                  [self.ingrediente1],
                                  2)
        self.torta=Torta("pan di spagna",["crema alla nocciola","crema al pistacchio"],"panna montata",15.00,0.5,"torta per 4 persone")
        self.cliente = Cliente("Mario","Rossi","mariorossi@gmail.com","Gino_pino40!","3415640891",[],[],[])
        self.ordine1 = Ordine([self.prodotto1,self.prodotto2],"10-09-2023",self.cliente,"Negozio",data_consegna,False)
        self.ordine2 = Ordine(self.torta,"11-09-2023",self.cliente,"Negozio",data_consegna,False)
        self.controller_ordine1 = ControllerOrdine(self.ordine1)
        self.controller_ordine2 = ControllerOrdine(self.ordine2)


    def tearDown(self):
        # Pulisco i dati di test dopo ciascun test
        self.controller_ordine1=None
        self.controller_ordine2 = None

    def test_get_lista_prodotti_ordinati(self):

        # Ottengo la lista dei prodotti ordinati
        lista_prodotti_ordinati1 = self.controller_ordine1.get_lista_prodotti_ordinati()
        lista_prodotti_ordinati2 = self.controller_ordine2.get_lista_prodotti_ordinati()
        # Verifico che la lista contenga gli stessi prodotti che ho aggiunto all'ordine1
        self.assertEqual(lista_prodotti_ordinati1, [self.prodotto1, self.prodotto2])
        self.assertEqual(lista_prodotti_ordinati2, self.torta)

    def test_get_importo(self):

        # Calcola l'importo atteso per l ordine 1 e 2
        importo_atteso1 = self.prodotto1.prezzo*self.prodotto1.quantita + self.prodotto2.prezzo*self.prodotto2.quantita
        importo_atteso2 = self.torta.prezzo
        # Ottieni l'importo calcolato dal ControllerOrdine
        importo_calcolato1 = self.controller_ordine1.get_importo()
        importo_calcolato2 = self.controller_ordine2.get_importo()
        # Verifico che l'importo calcolato corrisponda all'importo atteso
        self.assertEqual(importo_calcolato1, importo_atteso1)
        self.assertEqual(importo_calcolato2, importo_atteso2)

    def test_completa_ordine(self):
        # Verifico che l'ordine non sia completato inizialmente
        self.assertFalse(self.ordine1.completato)

        # Eseguo la funzione completa_ordine
        self.controller_ordine1.completa_ordine()

        # Verifico che l'ordine sia ora completato
        self.assertTrue(self.ordine1.completato)

    def test_get_nome_cliente(self):
        # Ottengo il nome del cliente dall'ordine tramite il controller
        nome_cliente = self.controller_ordine1.get_nome_cliente()

        # Verifico che il nome del cliente ottenuto corrisponde a quello atteso
        self.assertEqual(nome_cliente, "Mario")

    def test_get_data_consegna(self):
        # Ottengo la data di consegna formattata dall'ordine tramite il controller
        data_consegna = self.controller_ordine1.get_data_consegna()

        # Verifico che la data di consegna ottenuta corrisponda a quella attesa
        self.assertEqual(data_consegna, "23/09/2023 15:30")







