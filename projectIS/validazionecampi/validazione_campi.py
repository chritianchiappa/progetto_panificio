import re


class Validation:
    def __init__(self):
        self.patternPassword = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
        self.patternEmail = r'^[\w.-]+@[\w.-]+\.\w+$'
        self.patternTelefono = r'^\d{10}$'

    def val_email(self, email):
        return re.match(self.patternEmail, email) is None

    def val_password(self, password):
        return re.match(self.patternPassword, password) is None

    def val_telefono(self, telefono):
        return re.match(self.patternTelefono, telefono) is None
