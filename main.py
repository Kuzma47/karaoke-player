from PyQt5.QtWidgets import QApplication
from Window import Window

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.showMaximized()
    app.exec()
    window.karaoke.stop_karaoke()
