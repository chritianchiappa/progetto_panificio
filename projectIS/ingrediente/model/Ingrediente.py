class Ingrediente:
    def __init__(self, nome,prezzo,quantita,allergeni,scadenza):
        super(Ingrediente, self).__init__()
        self.nome=nome
        self.prezzo=prezzo
        self.quantita=quantita
        self.allergeni=allergeni
        self.scadenza=scadenza