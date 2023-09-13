import unittest
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from prodotto.controller.ControllerProdotto import ControllerProdotto
from ingrediente.model.Ingrediente import Ingrediente
from prodotto.model.Prodotto import Prodotto

class TestProdotti(unittest.TestCase):
    def loadData(self):
        self.controller_listaprodotti = ControllerListaProdotti()
        self.model_lista_prodotti = self.controller_listaprodotti.get_lista_prodotti()
        self.ingrediente1=Ingrediente("farina 00",1.24,10,"Kg",["glutine"],"31-12-2023")
        self.ingrediente2=Ingrediente("uova",0.50,10,"Pz",["uova"],"31-12-2023")
        self.prodotto = Prodotto("Ciambellone",
                                 "Dolci",
                                 16.00,
                                 [self.ingrediente1,self.ingrediente2],
                                 12)

        self.controller_prodotto = ControllerProdotto(self.prodotto)

    def test_inserisci_prodotto(self):
        self.assertIsNotNone(self.prodotto)
        self.controller_listaprodotti.inserisci_prodotto(self.prodotto)
        self.assertIn(self.prodotto,self.model_lista_prodotti)

    def test_check_prodotto(self):
        self.controller_listaprodotti.inserisci_prodotto(self.prodotto)
        result = self.controller_listaprodotti.check_prodotto("Ciambellone")
        self.assertIsNotNone(result)
        self.assertEqual(result.quantita,12)


    def aggiorna_quantita_prodotto(self):

    def test_rimuovi_prodotto_by_index(self):
        # Assumi che ci sia almeno un prodotto nella lista
        initial_length = len(self.model_lista_prodotti)

        # Rimuovi un prodotto (assicurati di avere un indice valido)
        index_to_remove = 0
        self.controller_listaprodotti.rimuovi_prodotto_by_index(index_to_remove)

        # Verifica se il prodotto è stato rimosso correttamente
        self.assertEqual(len(self.model_lista_prodotti), initial_length - 1)

    def get_prodotto_by_index(self):


if __name__ == '__main__':
    unittest.main()