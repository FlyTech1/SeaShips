import sys

from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from Window import Ui_MainWindow

from PySide6.QtGui import QDesktopServices, QCursor
from PySide6.QtCore import QUrl, Qt
class Window_main(QMainWindow):
    def __init__(self):
        super(Window_main,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget_2.hide()
        self.ui.PB_Play.clicked.connect(self.on_PB_Play_clicked)
        self.ui.PB_TG.clicked.connect(self.on_PB_TG_clicked)
        self.ui.PB_Rules.clicked.connect(self.on_PB_Rules_clicked)
        self.dragging=False
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

    def mouseMoveEvent(self, event):
        print("123")
        if self.dragging:
            self.ui.Ship_1.move(event.pos() - self.offset)
    def mousePressEvent(self, event):
        if(event.buttons()==Qt.MouseButton.LeftButton and self.ui.Ship_1.geometry().contains(event.pos())):
            self.dragging = True
            print("123")
            self.offset=event.pos()-self.ui.Ship_1.pos()
            print(event.pos())
            print(self.offset)



    def mouseReleaseEvent(self, event):
        self.dragging = False


