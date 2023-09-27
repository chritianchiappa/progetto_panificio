from PyQt6.QtWidgets import QSplashScreen,QApplication
from PyQt6 import uic
from PyQt6.QtCore import Qt,QTimer

from login.view.VistaLogin import VistaLogin
COUNTER=0
class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen,self).__init__()
        uic.loadUi('splashscreen/view/splashScreen.ui',self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.centerOnScreen()
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(60)
        self.dettagli_caricamento.setText("Caricamento...")
        QTimer.singleShot(1500, lambda: self.dettagli_caricamento.setText("Caricamento dati..."))
        QTimer.singleShot(3500, lambda: self.dettagli_caricamento.setText("Caricamento software..."))
        QTimer.singleShot(5400, lambda: self.dettagli_caricamento.setText("Avvio..."))


    def progress(self):
        global COUNTER
        self.progressBar.setValue(COUNTER)
        self.percentage.setText(f"{int(COUNTER)}%")
        if COUNTER>100:
            self.timer.stop()
            self.login=VistaLogin()
            self.close()
            self.login.show()
        COUNTER+=1

    def centerOnScreen(self): #serve per centrare lo splashscreen
        available_geometry = QApplication.primaryScreen().availableGeometry()
        self.move(
            available_geometry.center() - self.rect().center()
        )
