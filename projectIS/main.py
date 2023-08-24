import sys
from PyQt6.QtWidgets import QApplication

from home.view.VistaLogin import VistaLogin
from splashscreen.view.SplashScreen import SplashScreen
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash=SplashScreen()
    splash.show()

    sys.exit(app.exec())



