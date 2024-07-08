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
        self.ui.PB_Play.clicked.connect(self.on_PB_Play_clicked)
        self.ui.PB_TG.clicked.connect(self.on_PB_TG_clicked)
    def on_PB_Play_clicked(self):
        self.game_menu_window=Window_Game_Menu()
        self.game_menu_window.setParent(self)
        self.game_menu_window.show()
        #self.hide()
    def on_PB_TG_clicked(self):
        print("NEGRI")
        url=QUrl("https://t.me/bezdariprogaut")
        QDesktopServices.openUrl(url)



