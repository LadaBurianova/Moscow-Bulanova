import sys
from PyQt5 import uic
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_obj(qp)
            qp.end()

    def draw_obj(self, qp):
        diam = randint(1, 300)
        x = randint(0, self.width() - diam)
        y = randint(0, self.height() - diam)
        qp.setBrush(QColor(255, 204, 0))  # Цвет Яндекса
        qp.drawEllipse(x, y, diam, diam)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
