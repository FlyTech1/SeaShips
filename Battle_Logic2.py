from PySide6.QtWidgets import QMainWindow
from game_menu import Ui_game_menu


class Window_Game_Menu(QMainWindow):
    def __init__(self):
        super(Window_Game_Menu, self).__init__()
        self.ui = Ui_game_menu()
        self.ui.setupUi(self)
