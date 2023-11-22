import sys
from random import random, randint
import math

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QPushButton, QInputDialog, QColorDialog
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic


class DrawTheSun(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.flag = 0
        self.runButton.clicked.connect(self.run)

    def run(self):
        self.flag = 1
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_figure(qp)
            qp.end()

    def draw_figure(self, qp):
        size = randint(20, 300)
        qp.setBrush(QColor('yellow'))
        qp.eraseRect(0, 0, 1000, 1000)
        qp.drawEllipse(self.width() // 2 - size // 2, self.height() // 2 - size // 2, size, size)
        self.flag = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawTheSun()
    ex.show()
    sys.exit(app.exec())
