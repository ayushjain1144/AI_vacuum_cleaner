#########################

#NAME: AYUSH JAIN
#ID: 2017A7PS0093P

#########################
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import config

class Ball(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        pix = QPixmap("vacuum.jpg")
        self.h = pix.height()
        self.w = pix.width()
        pixmap2 = pix.scaled(40, 40, Qt.KeepAspectRatio)
        self.setPixmap(pixmap2)

    def _set_pos(self, pos):

        self.move(pos.x(), pos.y())

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Current_State(QWidget):

    def __init__(self, state, size):
        super().__init__()

        self.state = state
        self.size = size
        self.initUI()

    def initUI(self):

        self.resize(1000, 1000)
        self.center()
        self.setWindowTitle('Current_State')


        self.ball_bfs = Ball(self)
        half_width = (1000 / self.size) / 2
        self.ball_bfs.pos = QPointF(half_width, half_width)

        self.show()
        
    def dirt_gui(self, qp):

        row = self.size
        col = self.size
        floor  = self.state.floor

        grey = 0xA9A9A9
        white = 0xffffff
        init_x = 0
        init_y = 0
        x = init_x
        y = init_y
        width = 1000 / self.size
        height = 1000 / self.size


        for i, j in enumerate(floor, 1):



            if j:
                self.drawRectangles(qp, x, y, width, height, grey)
                x = x + width
            else:
                self.drawRectangles(qp, x, y, width, height, white)
                x = x + width

            if(i % col == 0):
                y = y + height
                x = init_x

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.dirt_gui(qp)
        qp.end()

    def center(self):

        qr = self.frameGeometry()
        cp  = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def drawRectangles(self, qp, x, y, width, height, color):

        qp.setBrush(QColor(color))
        qp.drawRect(x, y, width, height)
