class ControllerProdotto:
    def __init__(self,prodotto):
        self.model = prodotto

    def get_lista_ingredienti(self):
        return self.model.ingredienti
    def get_prezzo(self):
        p=self.model.prezzo
        q=self.model.quantita
        return p*q

    def get_allergeni(self):
        lista_allergeni=[]
        for ingrediente in self.get_lista_ingredienti():
            for allergene in ingrediente.allergeni:
                if allergene not in lista_allergeni:
                    lista_allergeni.append(allergene)
        return lista_allergeni
    def get_nome(self):
        return self.model.nome