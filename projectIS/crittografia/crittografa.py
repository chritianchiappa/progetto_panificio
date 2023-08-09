from cryptography.fernet import Fernet

#modifica michele 6.0
class CryptoManager:
    def __init__(self):
        self.key = b'QaywJxlWb6nOrEt5X1zZawGstHK5sAWfUQpSejYhXIQ='

    def cripta_dati(self, dati):
        fernet = Fernet(self.key)
        dati_criptati = fernet.encrypt(dati)
        return dati_criptati

    def decrittografa_dati(self, dati_criptati):
        fernet = Fernet(self.key)
        dati_decriptati = fernet.decrypt(dati_criptati)
        return dati_decriptati

