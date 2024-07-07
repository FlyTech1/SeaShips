# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import res_rc

class Ui_game_menu(object):
    def setupUi(self, game_menu):
        if not game_menu.objectName():
            game_menu.setObjectName(u"game_menu")
        game_menu.resize(800, 650)
        game_menu.setStyleSheet(u"background-color: #009eff")
        self.centralwidget = QWidget(game_menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(660, 190, 41, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 230, 51, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 260, 71, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(660, 300, 101, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 40, 281, 91))
        game_menu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(game_menu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        game_menu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(game_menu)
        self.statusbar.setObjectName(u"statusbar")
        game_menu.setStatusBar(self.statusbar)

        self.retranslateUi(game_menu)

        QMetaObject.connectSlotsByName(game_menu)
    # setupUi

    def retranslateUi(self, game_menu):
        game_menu.setWindowTitle(QCoreApplication.translate("game_menu", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("game_menu", u"<html><head/><body><p><img src=\":/models/Models ships/ship1.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("game_menu", u"<html><head/><body><p><img src=\":/models/Models ships/ship2.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("game_menu", u"<html><head/><body><p><img src=\":/models/Models ships/ship3.png\"/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("game_menu", u"<html><head/><body><p><img src=\":/models/Models ships/ship4.png\"/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("game_menu", u"\u0420\u0430\u0441\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0440\u0430\u0431\u043b\u0438  \u0432 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0435", None))
    # retranslateUi

