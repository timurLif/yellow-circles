import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Random Circles')
        
        self.button.clicked.connect(self.drawCircle)

        self.circles = []

    def drawCircle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(Qt.yellow)

        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleDrawer()
    ex.show()
    sys.exit(app.exec_())
