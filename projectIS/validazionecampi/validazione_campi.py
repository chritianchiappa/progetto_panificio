import re

class Validation:
    def __init__(self):
        #definisco dei pattern per i vari campi di cui voglio fare la validazione
        self.patternPassword = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
        self.patternEmail = r'^[\w.-]+@[\w.-]+\.\w+$'
        self.patternTelefono = r'^\d{10}$'
        self.patternCFiscale=r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$'

    #queste funzioni servono per determinare se il valore contenuto nel campo matcha con il relativo pattern o meno
    def val_email(self, email):
        return re.match(self.patternEmail, email) is None

    def val_password(self, password):
        return re.match(self.patternPassword, password) is None

    def val_telefono(self, telefono):
        return re.match(self.patternTelefono, telefono) is None
    def val_cfiscale(self,cfiscale):
        return re.match(self.patternCFiscale, cfiscale) is None

