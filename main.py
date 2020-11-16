import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPainterPath
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.runDraw)
        self.flag = False
        self.qp = QPainter()

    def getRandomSize(self):
        size = random.randint(20, 100)
        return size, size

    def getRandomCoords(self):
        return [random.randint(0, 300), random.randint(0, 300)]

    def runDraw(self):
        self.flag = True
        self.repaint()

    def draw(self):
        self.qp.drawEllipse(*self.getRandomCoords(), *self.getRandomSize())

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            self.draw()
            self.qp.end()
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())