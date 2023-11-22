import sys
from random import random, randint
import math

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QPushButton, QInputDialog, QColorDialog
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic
from UI import Ui_MainWindow

class DrawTheSun(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = 0
        self.runButton.clicked.connect(self.run)
        self.setWindowTitle('Git и случайные окружности')

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
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.eraseRect(0, 0, 1000, 1000)
        qp.drawEllipse(self.width() // 2 - size // 2, self.height() // 2 - size // 2, size, size)
        self.flag = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawTheSun()
    ex.show()
    sys.exit(app.exec())
