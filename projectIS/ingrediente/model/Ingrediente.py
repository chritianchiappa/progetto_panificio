
class Ingrediente:
    def __init__(self, nome,prezzo,unita_misura,quantita,allergeni,scadenza):
        super(Ingrediente, self).__init__()
        self.nome=nome
        self.prezzo=prezzo
        self.unita_misura=unita_misura
        self.quantita=quantita
        self.allergeni=allergeni
        self.scadenza=scadenza