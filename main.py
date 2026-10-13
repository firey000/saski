import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from mainWindow import Ui_MainWindow
from mainPage import Ui_Form as Menu
from gamePage import Ui_Form as Game
from settingsPage import Ui_Form as Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stackedWidget = self.ui.stackedWidget
        self.menuPage = MenuPage(self)
        self.gamePage = GamePage(self)

        self.stackedWidget.addWidget(self.gamePage)
        self.stackedWidget.addWidget(self.menuPage)
        self.stackedWidget.setCurrentWidget(self.menuPage)

    def show_game(self):
        self.stackedWidget.setCurrentWidget(self.gamePage)

    def show_menu(self):
        self.stackedWidget.setCurrentWidget(self.menuPage)


class GamePage(QWidget):
    def __init__(self, parent_win):
        super().__init__()
        self.parent_window = parent_win
        self.ui = Game()
        self.ui.setupUi(self)

        self.ui.exitBtn.clicked.connect(self.parent_window.show_menu)

class MenuPage(QWidget):
    def __init__(self, parent_win):
        super().__init__()
        self.parent_window = parent_win
        self.ui = Menu()
        self.ui.setupUi(self)

        self.ui.exitBtn.clicked.connect(self.parent_window.close)
        self.ui.igratBtn.clicked.connect(self.parent_window.show_game)

class SettingsPage(QWidget):
    def __init__(self, parent_win):
        super().__init__()
        self.parent_window = parent_win
        self.ui = Settings()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
