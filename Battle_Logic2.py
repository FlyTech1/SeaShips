#Creating
from PySide6.QtWidgets import QMainWindow
from game_menu import Ui_game_menu
#Import
from  PySide6.QtCore import Qt
#Work Anton
class Window_Game_Menu(QMainWindow):
    def __init__(self):
        super(Window_Game_Menu, self).__init__()
        self.ui = Ui_game_menu()
        self.ui.setupUi(self)
        self.dragging = False

    def update_style(self, color):
        self.setStyleSheet(f"""
            border: 2px solid black;
            border-radius: 5px;
            border-color: {color};
        """)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.drag_start_position)
            self.parent().check_widget_position(self)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
    def check_widget_position(self, widget):
        label_rect = self.ui.label.geometry()
        widget_rect = widget.geometry()

        if label_rect.contains(widget_rect.topLeft()) and label_rect.contains(widget_rect.bottomRight()):
            widget.update_style("green")
        else:
            widget.update_style("red")