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
import res_rc_rc

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
        self.PB_TG_2 = QPushButton(self.widget)
        self.PB_TG_2.setObjectName(u"PB_TG_2")
        self.PB_TG_2.setGeometry(QRect(10, 20, 70, 70))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(52)
        font1.setBold(True)
        self.PB_TG_2.setFont(font1)
        self.PB_TG_2.setStyleSheet(u"image: url(:/icon/icons/1-20-2048x2011.png);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;")
        self.PB_TG_2.setIconSize(QSize(32, 32))
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
        self.widget_2.setGeometry(QRect(10, 10, 800, 650))
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 10, 301, 91))
        self.pushButton.setStyleSheet(u"font: 9pt \"MS Sans Serif\";\n"
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 0, 411, 351))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(640, 170, 41, 41))
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(640, 250, 71, 51))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(640, 300, 101, 41))
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 210, 51, 31))
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 490, 291, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Battle Ships", None))
        self.PB_TG_2.setText("")
        self.PB_Rules.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.PB_Play.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0440\u0430\u0431\u043b\u0438  \u0432 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0435", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/ModelsShips/Models ships/ship1.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/ModelsShips/Models ships/ship3.png\"/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/ModelsShips/Models ships/ship4.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/ModelsShips/Models ships/ship2.png\"/></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0421\u041d\u0418 \u041c\u0415\u041d\u042f", None))
    # retranslateUi

