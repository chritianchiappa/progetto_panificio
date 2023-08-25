from PyQt6.QtWidgets import QSplashScreen,QApplication
from PyQt6 import uic
from PyQt6.QtCore import Qt,QTimer,QPropertyAnimation,QEasingCurve

from home.view.VistaLogin import VistaLogin
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
        #self.logo_animation()
        self.dettagli_caricamento.setText("Caricamento...")
        QTimer.singleShot(1500, lambda: self.dettagli_caricamento.setText("Caricamento dati..."))
        QTimer.singleShot(3500, lambda: self.dettagli_caricamento.setText("Caricamento software..."))
        QTimer.singleShot(5400, lambda: self.dettagli_caricamento.setText("Avvio..."))
    #def logo_animation(self):
        #animation = QPropertyAnimation(self.logo, b"opacity")
        #animation.setStartValue(0.0)
        #animation.setEndValue(1.0)
        #animation.setDuration(1000)
        #easing_curve = QEasingCurve(QEasingCurve.Type.Linear)
        #animation.setEasingCurve(easing_curve)
        #animation.start()

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

    def centerOnScreen(self):
        available_geometry = QApplication.primaryScreen().availableGeometry()
        self.move(
            available_geometry.center() - self.rect().center()
        )
