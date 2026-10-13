import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem

from mainWindow import Ui_MainWindow
from mainPage import Ui_Form as Menu
from gamePage import Ui_Form as Game


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


class GamePage(QWidget):
    def __init__(self, parent_win):
        super().__init__()
        self.parent_window = parent_win
        self.ui = Game()
        self.ui.setupUi(self)



        for i in range(0, 8):
            for j in range(i % 2, 8, 2):
                item = self.ui.tableWidget.item(i, j)
                item.setBackground(QBrush(QColor(255, 0, 0)))


class MenuPage(QWidget):
    def __init__(self, parent_win):
        super().__init__()
        self.parent_window = parent_win
        self.ui = Menu()
        self.ui.setupUi(self)

        self.ui.exitBtn.clicked.connect(self.close_window)
        self.ui.igratBtn.clicked.connect(self.show_game)

    def close_window(self):
        self.parent_window.close()

    def show_game(self):
        self.parent_window.show_game()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
