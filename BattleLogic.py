import sys

from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from Window import Ui_MainWindow

from PySide6.QtGui import QDesktopServices
from PySide6 import  QtGui, QtCore
from PySide6.QtCore import QUrl
class Window_main(QMainWindow):
    def __init__(self):
        super(Window_main,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget_2.hide()
        self.ui.PB_Play.clicked.connect(self.on_PB_Play_clicked)
        self.ui.PB_TG.clicked.connect(self.on_PB_TG_clicked)
        self.ui.PB_Rules.clicked.connect(self.on_PB_Rules_clicked)
    def on_PB_Play_clicked(self):
        self.ui.widget.hide()
        self.ui.widget_2.show()
        #self.hide()
    def on_PB_TG_clicked(self):
        url1=QUrl("https://t.me/bezdariprogaut")
        QDesktopServices.openUrl(url1)
    def on_PB_Rules_clicked(self):
        url2 = QUrl("https://PORNOHUB/CASINO/MEF.ru")
        QDesktopServices.openUrl(url2)


