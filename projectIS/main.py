import sys
from PyQt6.QtWidgets import QApplication


from splashscreen.view.SplashScreen import SplashScreen
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash=SplashScreen()
    splash.show()

    sys.exit(app.exec())



