# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gamePage.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1121, 830)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.giveUpBtn = QPushButton(Form)
        self.giveUpBtn.setObjectName(u"giveUpBtn")
        self.giveUpBtn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.giveUpBtn)

        self.exitBtn = QPushButton(Form)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(150, 35))

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.turnLabel = QLabel(Form)
        self.turnLabel.setObjectName(u"turnLabel")
        font = QFont()
        font.setPointSize(16)
        self.turnLabel.setFont(font)

        self.horizontalLayout.addWidget(self.turnLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.timeLabel = QLabel(Form)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font)

        self.horizontalLayout.addWidget(self.timeLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(brush)
        self.tableWidget.setItem(0, 0, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(8)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.giveUpBtn.setText(QCoreApplication.translate("Form", u"\u0421\u0434\u0430\u0442\u044c\u0441\u044f", None))
        self.exitBtn.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.turnLabel.setText(QCoreApplication.translate("Form", u"\u0425\u043e\u0434 \u0441\u0430\u0445\u0430\u0440\u043e\u0447\u043a\u0430", None))
        self.timeLabel.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"8", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

