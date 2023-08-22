import sys
from PyQt6.QtWidgets import QApplication

from home.view.VistaLogin import VistaLogin

if __name__ == "__main__":

    app = QApplication(sys.argv)
    login = VistaLogin()
    login.show()
    sys.exit(app.exec())



