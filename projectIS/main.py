import sys
from PyQt6.QtWidgets import QApplication
import shutil
import datetime
import os
import time
import threading

files_to_backup = ['listaspese/data/lista_spese_salvata.pickle',
                   'listaprodotti/data/lista_prodotti_salvata.pickle',
                   'listaordini/data/lista_ordini_salvata.pickle',
                   'listaingredienti/data/lista_ingredienti_salvata.pickle',
                   'listadipendenti/data/lista_dipendenti_salvata.pickle',
                   'listaclienti/data/lista_clienti_salvata.pickle']
def backup_files():
    current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.now().date()

    # Verifica se l'orario corrente è 23:30
    if current_time.hour == 23 and current_time.minute == 30:
        backup_base_dir = 'backup/'
        os.makedirs(backup_base_dir, exist_ok=True)

        current_time_str = current_day.strftime("%d.%m.%Y")
        backup_dir = os.path.join(backup_base_dir, current_time_str)
        os.makedirs(backup_dir, exist_ok=True)
        for source_file in files_to_backup:
            # Verifica se il file di origine esiste prima di eseguire il backup
            if os.path.exists(source_file):
                 # Copia il file originale nella cartella di backup
                shutil.copy(source_file, backup_dir)


            else:

                print(f'Il file {source_file} non esiste, il backup non è stato eseguito per questo file.')
    else:
        print('Non è l\'orario programmato per il backup.')
def backup_thread():
    while True:
        backup_files()
        # Aspetta 59 secondi prima di verificare nuovamente l'orario
        time.sleep(59)
from splashscreen.view.SplashScreen import SplashScreen
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash=SplashScreen()
    splash.show()
    # Avvia il thread di backup in background
    backup_thread = threading.Thread(target=backup_thread)
    backup_thread.daemon = True
    backup_thread.start()

    sys.exit(app.exec())






