# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
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
        MainWindow.setStyleSheet(u"background-color: #008bd0")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 650))
        self.PB_TG = QPushButton(self.widget)
        self.PB_TG.setObjectName(u"PB_TG")
        self.PB_TG.setGeometry(QRect(10, 20, 70, 70))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(52)
        font1.setBold(True)
        self.PB_TG.setFont(font1)
        self.PB_TG.setStyleSheet(u"image: url(:/icons/icons/1-20-2048x2011.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;")
        self.PB_TG.setIconSize(QSize(32, 32))
        self.PB_Rules = QPushButton(self.widget)
        self.PB_Rules.setObjectName(u"PB_Rules")
        self.PB_Rules.setGeometry(QRect(200, 350, 400, 100))
        self.PB_Rules.setFont(font1)
        self.PB_Rules.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.PB_Rules.setIconSize(QSize(32, 32))
        self.PB_Play = QPushButton(self.widget)
        self.PB_Play.setObjectName(u"PB_Play")
        self.PB_Play.setGeometry(QRect(200, 200, 400, 100))
        self.PB_Play.setMinimumSize(QSize(400, 0))
        self.PB_Play.setMaximumSize(QSize(400, 16777215))
        self.PB_Play.setFont(font1)
        self.PB_Play.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.PB_Play.setIconSize(QSize(32, 32))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 800, 650))
        font2 = QFont()
        font2.setFamilies([u"Script"])
        self.widget_2.setFont(font2)
        self.widget_2.setStyleSheet(u"background-color:#009eff;")
        self.Random_pos_ships = QPushButton(self.widget_2)
        self.Random_pos_ships.setObjectName(u"Random_pos_ships")
        self.Random_pos_ships.setGeometry(QRect(570, 10, 200, 100))
        font3 = QFont()
        font3.setFamilies([u"MS Sans Serif"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.Random_pos_ships.setFont(font3)
        self.Random_pos_ships.setStyleSheet(u"font: 9pt \"MS Sans Serif\";\n"
"background-color: white;\n"
"border-radius: 25px;")
        self.tableWidget = QTableWidget(self.widget_2)
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
        for i in range(10):
            self.tableWidget.setColumnWidth(i,48)
        for i in range(10):
            self.tableWidget.setRowHeight(i,45)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 540, 500))
        #self.tableWidget.setStyleSheet("QTableWidget { border: none; }")
        self.Ship_1 = QLabel(self.widget_2)
        self.Ship_1.setObjectName(u"Ship_1")
        self.Ship_1.setGeometry(QRect(640, 170, 41, 41))
        self.Ship_3 = QLabel(self.widget_2)
        self.Ship_3.setObjectName(u"Ship_3")
        self.Ship_3.setGeometry(QRect(640, 250, 71, 51))
        self.Ship_4 = QLabel(self.widget_2)
        self.Ship_4.setObjectName(u"Ship_4")
        self.Ship_4.setGeometry(QRect(640, 300, 101, 41))
        self.Ship_2 = QLabel(self.widget_2)
        self.Ship_2.setObjectName(u"Ship_2")
        self.Ship_2.setGeometry(QRect(640, 210, 51, 31))
        self.User_ready = QPushButton(self.widget_2)
        self.User_ready.setObjectName(u"User_ready")
        self.User_ready.setGeometry(QRect(240, 490, 291, 71))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift SemiCondensed"])
        font4.setPointSize(28)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.User_ready.setFont(font4)
        self.User_ready.setStyleSheet(u"background-color: white;\n"
"border: 1px solid black;\n"
"border-radius: 25px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_2.raise_()
        self.widget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Battle Ships", None))
        self.PB_TG.setText("")
        self.PB_Rules.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.PB_Play.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.Random_pos_ships.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0440\u0430\u0431\u043b\u0438  \u0432 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0435", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0410", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0411", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0412", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0413", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0414", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0415", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0416", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0417", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0418", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041a", None));
        self.Ship_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Models_Ships/Models ships/ship1.png\"/></p></body></html>", None))
        self.Ship_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Models_Ships/Models ships/ship3.png\"/></p></body></html>", None))
        self.Ship_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Models_Ships/Models ships/ship4.png\"/></p></body></html>", None))
        self.Ship_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Models_Ships/Models ships/ship2.png\"/></p></body></html>", None))
        self.User_ready.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432!", None))
    # retranslateUi

