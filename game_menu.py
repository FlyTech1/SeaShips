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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)
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
        self.pushButton.setGeometry(QRect(480, 40, 301, 91))
        self.pushButton.setStyleSheet(u"font: 9pt \"MS Sans Serif\";\n"
"background-color: white;\n"
"border-radius: 25px;")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 130, 591, 401))
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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("game_menu", u"\u0410", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("game_menu", u"\u0411", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("game_menu", u"\u0412", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("game_menu", u"\u0413", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("game_menu", u"\u0414", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("game_menu", u"\u0415", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("game_menu", u"\u0416", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("game_menu", u"\u0417", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("game_menu", u"\u0418", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("game_menu", u"\u041a", None));
    # retranslateUi

