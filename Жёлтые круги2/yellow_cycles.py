import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setupUi(self)
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
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, diam, diam)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
