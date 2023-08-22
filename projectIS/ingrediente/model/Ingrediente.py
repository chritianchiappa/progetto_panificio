class Ingrediente:
    def __init__(self, nome,prezzo,tipo,quantita,allergeni,scadenza):
        super(Ingrediente, self).__init__()
        self.nome=nome
        self.prezzo=prezzo
        self.quantita=quantita
        self.allergeni=allergeni
        self.tipo=tipo
        self.scadenza=scadenza