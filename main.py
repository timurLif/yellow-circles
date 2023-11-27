import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor


class CircleDrawerUI(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('Draw Circle', self)
        self.button.setGeometry(10, 0, 520, 30)


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = CircleDrawerUI()
        self.setCentralWidget(self.ui)

        self.ui.button.clicked.connect(self.drawCircle)

        self.circles = []

    def drawCircle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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
    ex.setWindowTitle('Random Circles')
    ex.setGeometry(0, 0, 540, 600)
    ex.show()
    sys.exit(app.exec_())