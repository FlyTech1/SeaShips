from BattleLogic import Window_main
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window_main()
    w.setFixedSize(800,650)
    w.show()
    sys.exit(app.exec())
