# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 650)
        font = QFont()
        font.setFamilies([u"Ravie"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #009eff")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 270, 361, 91))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(52)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 380, 361, 91))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 20, 71, 71))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"image: url(:/icon/icons/1-20-2048x2011.png);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;")
        self.pushButton_3.setIconSize(QSize(32, 32))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Battle Ships", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.pushButton_3.setText("")
    # retranslateUi

