import sys

from PySide6.QtGui import QBrush, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem
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

class GamePage(QDialog):
    def __init__(self, parent_win):
        super().__init__(parent_win)
        self.ui = Game()
        self.ui.setupUi(self)
        self.parent_window = parent_win

        self.item = QTableWidgetItem()
        self.brush = QBrush()
        self.brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.item.setBackground(self.brush)
        for i in range(0, 8, 2):
            for j in range(0 + i % 2, 8):
                self.ui.tableWidget.setItem(i, j, self.item)


class MenuPage(QDialog):
    def __init__(self, parent_win):
        super().__init__(parent_win)
        self.ui = Menu()
        self.ui.setupUi(self)
        self.parent_window = parent_win






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())