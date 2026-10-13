import sys
from PySide6 import QMainWindow
from PySide6.QtWidgets import QApplication, QDialog

from mainWindow import Ui_MainWindow
from mainPage import Ui_Form as Menu
from gamePage import Ui_Form as Game


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stakedWidget = self.ui.stackedWidget()
        self.menuPage = MenuPage(self)
        self.gamePage = GamePage(self)

        self.stakedWidget.addWidget(self.gamePage)
        self.stackedWidget.addWidget(self.menuPage)
        self.stackedWidget.setCurrentWidget(self.menuPage)

    def show_game(self):
        self.stakedWidget.setCurrentWidget(self.gamePage)

class GamePage(QDialog):
    def __init__(self, parent_win):
        super().__init__(parent_win)
        self.ui = Game()
        self.ui.setupUi(self)
        self.parent_window = parent_win


class MenuPage(QDialog):
    def __init__(self, parent_win):
        super().__init__(parent_win)
        self.ui = Menu()
        self.ui.setupUi(self)
        self.parent_window = parent_win






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec())