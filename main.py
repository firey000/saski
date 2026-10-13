import sys

from PySide6 import QMainWindow
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec())