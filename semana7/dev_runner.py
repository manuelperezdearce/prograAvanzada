import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Ruta base del proyecto
BASE_PATH = os.getcwd()
MAIN_FILE = "index.py"  # archivo principal que se debe reiniciar

class AutoReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart_program()

    def restart_program(self):
        # Si ya hay un proceso corriendo, lo mata
        if self.process:
            self.process.kill()
            print("\n[INFO] Reiniciando programa...\n")
        # Lanza el programa principal
        self.process = subprocess.Popen([sys.executable, MAIN_FILE])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"[INFO] Cambio detectado en {os.path.basename(event.src_path)}")
            self.restart_program()

def main():
    print("[INFO] Auto-Reload ACTIVADO. Guardar archivos reiniciará automáticamente.\n")
    event_handler = AutoReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, BASE_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Deteniendo Auto-Reload...")
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()

if __name__ == "__main__":
    main()