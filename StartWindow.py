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
        self.PB_Play = QPushButton(self.centralwidget)
        self.PB_Play.setObjectName(u"PB_Play")
        self.PB_Play.setGeometry(QRect(200, 200, 400, 100))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(52)
        font1.setBold(True)
        self.PB_Play.setFont(font1)
        self.PB_Play.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.PB_Play.setIconSize(QSize(32, 32))
        self.PB_Rules = QPushButton(self.centralwidget)
        self.PB_Rules.setObjectName(u"PB_Rules")
        self.PB_Rules.setGeometry(QRect(200, 350, 400, 100))
        self.PB_Rules.setFont(font1)
        self.PB_Rules.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.PB_Rules.setIconSize(QSize(32, 32))
        self.PB_TG = QPushButton(self.centralwidget)
        self.PB_TG.setObjectName(u"PB_TG")
        self.PB_TG.setGeometry(QRect(10, 20, 71, 71))
        self.PB_TG.setFont(font1)
        self.PB_TG.setStyleSheet(u"image: url(:/icon/icons/1-20-2048x2011.png);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;")
        self.PB_TG.setIconSize(QSize(32, 32))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Battle Ships", None))
        self.PB_Play.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.PB_Rules.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.PB_TG.setText("")
    # retranslateUi

