import sys

from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from StartWindow import Ui_MainWindow
from game_menu import  Ui_game_menu

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
        self.game_menu_window.show()
        self.hide()
    def on_PB_TG_clicked(self):
        pass
        #label=QtGui.QLabel('<a href=""')



class Window_Game_Menu(QMainWindow):
    def __init__(self):
        super(Window_Game_Menu, self).__init__()
        self.ui = Ui_game_menu()
        self.ui.setupUi(self)
