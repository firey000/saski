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
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 35))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(8)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u0434\u0430\u0442\u044c\u0441\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0425\u043e\u0434 \u0441\u0430\u0445\u0430\u0440\u043e\u0447\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"8", None))
    # retranslateUi

