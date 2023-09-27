from cryptography.fernet import Fernet

class CryptoManager: #si occupa di crittografare i file pickle
    def __init__(self):
        self.key = b'QaywJxlWb6nOrEt5X1zZawGstHK5sAWfUQpSejYhXIQ='

    #attraverso l'utilizzo della chiave posso criptare e decriptare i dati

    def cripta_dati(self, dati):
        fernet = Fernet(self.key)
        dati_criptati = fernet.encrypt(dati)
        return dati_criptati

    def decrittografa_dati(self, dati_criptati):
        fernet = Fernet(self.key)
        dati_decriptati = fernet.decrypt(dati_criptati)
        return dati_decriptati

