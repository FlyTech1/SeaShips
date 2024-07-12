import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QDesktopServices, QCursor
from PySide6.QtCore import QUrl, Qt, QRect, QSize
from Window import Ui_MainWindow



class Window_main(QMainWindow):
    def __init__(self):
        super(Window_main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget_2.hide()
        self.ui.PB_Play.clicked.connect(self.on_PB_Play_clicked)
        self.ui.PB_TG.clicked.connect(self.on_PB_TG_clicked)
        self.ui.PB_Rules.clicked.connect(self.on_PB_Rules_clicked)
        self.setMouseTracking(True)
        self.dragging = False

        # Заменяем QLabel на DraggableLabel

        # self.ui.Ship_2 = DraggableLabel(self.ui.widget_2)
        # self.ui.Ship_2.setObjectName("Ship_2")
        # self.ui.Ship_2.setGeometry(QRect(640, 210, 51, 31))
        # self.ui.Ship_2.setStyleSheet("background-color: transparent;")
        # self.ui.Ship_2.setText('<img src=":/Models_Ships/Models ships/ship2.png"/>')
        #
        # self.ui.Ship_3 = DraggableLabel(self.ui.widget_2)
        # self.ui.Ship_3.setObjectName("Ship_3")
        # self.ui.Ship_3.setGeometry(QRect(640, 250, 71, 51))
        # self.ui.Ship_3.setStyleSheet("background-color: transparent;")
        # self.ui.Ship_3.setText('<img src=":/Models_Ships/Models ships/ship3.png"/>')
        #
        # self.ui.Ship_4 = DraggableLabel(self.ui.widget_2)
        # self.ui.Ship_4.setObjectName("Ship_4")
        # self.ui.Ship_4.setGeometry(QRect(640, 300, 101, 41))
        # self.ui.Ship_4.setStyleSheet("background-color: transparent;")
        # self.ui.Ship_4.setText('<img src=":/Models_Ships/Models ships/ship4.png"/>')

    def on_PB_Play_clicked(self):
        self.ui.widget.hide()
        self.ui.widget_2.show()

    def on_PB_TG_clicked(self):
        url1 = QUrl("https://t.me/bezdariprogaut")
        QDesktopServices.openUrl(url1)

    def on_PB_Rules_clicked(self):
        url2 = QUrl("https://PORNOHUB/CASINO/MEF.ru")
        QDesktopServices.openUrl(url2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window_main()
    main_window.show()
    sys.exit(app.exec())
