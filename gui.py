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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=450, height=450, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot1()

    def plot1(self):
        x = [10, 15, 20, 25]
        data = [0.06998, 7.228, 24.487, 2407.1308]
        ax = self.figure.add_subplot(111)
        ax.plot(x, data, label='IDFS')
        ax.set(xlabel = 'dirt(in %)', ylabel='time taken')
        ax.grid()
        ax.set_title('dirt% vs time(5 by 5 floor)')
        ax.legend(loc='best')
        self.draw()

class PlotCanvas_g3(FigureCanvas):

    def __init__(self, parent=None, width=450, height=450, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot1()

    def plot1(self):
        x = [3, 4, 5, 6, 7, 8]
        data = [0.000634, 0.0085, 9.5168, 17.932, 220.9546, 2350]
        ax = self.figure.add_subplot(111)
        ax.plot(x, data, 'r-', label='IDFS')

        x1 = [3, 4, 5, 6]
        data1 = [0.002, 0.99, 9.05, 1563]
        ax.plot(x1, data1, 'b-', label='BFS')

        ax.set(xlabel = 'size of floor', ylabel='time taken')
        ax.grid()
        ax.set_title('size vs time')
        ax.legend(loc='best')
        self.draw()




class AI_Vacuum(QWidget):

    def __init__(self, state, action_path_bfs, action_path_idfs):
        super().__init__()

        self.state = state
        self.action_path_bfs = action_path_bfs
        self.action_path_idfs = action_path_idfs
        #self.initdirt_gui()
        self.initUI()
        self.initAnimation_bfs()



    def initdirt_gui(self):

        self.resize(450, 450)
        self.center()
        self.setWindowTitle('AI Vacuum Cleaner')
        self.show()

    def Grid(self, grid):

        row = 5
        col = 5
        scene = QGraphicsScene()
        view = QGraphicsView()
        view.setScene(scene)

        red = QColor(qRgb(172, 50, 99))
        blue = QColor(qRgb(50, 150, 203))

        vLines = row + 1
        hLines = col + 1
        side = 90

        hor = 0
        ver = 0
        subdiv = row
        leftX, leftY = 0, 0
        rightX, rightY = subdiv * side, 0
        bottomX, bottomY =  0, 0
        topX, topY = 0, subdiv * side

        while ver < vLines:

            ver = ver + 1
            vLine = QLineF(bottomX, bottomY, topX, topY)
            bottomX, topX =  bottomX + side, topX + side
            scene.addLine(vLine, red)


        while hor < hLines:

            hor = hor + 1
            hLine = QLineF(leftX, leftY, rightX, rightY)
            leftY, rightY = leftY + side, rightY + side
            scene.addLine(hLine, blue)

        grid.addWidget(view)

    def dirt_gui(self, qp):

        row = 5
        col = 5
        floor  = self.state.floor
        #qp = QPainter()
        #qp.begin(self)

        grey = 0xA9A9A9
        white = 0xffffff
        init_x = 450
        init_y = 0
        x = init_x
        y = init_y
        width = 90
        height = 90

        for count in range(2):
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
            #self.draw_border(qp, init_x, init_y, 450, 450)

            init_x = 908
            init_y = 0
            x = init_x
            y = init_y


        #qp.end()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.dirt_gui(qp)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QColor(0xff0000))
        qp.drawPath(self.path_bfs)
        qp.drawPath(self.path_idfs)
        qp.end()

    def draw_border(self, qp, x , y, width, height):

        qp.setPen(QPen(Qt.green, Qt.SolidLine))
        qp.drawRect(x, y, width, height)

    def initUI(self):

        #grid = QGridLayout()
        #self.setLayout(grid)

        self.resize(1358, 900)
        self.center()
        self.setWindowTitle('AI Vacuum Cleaner')



        hbox = QHBoxLayout(self)
        left = QVBoxLayout()


        lb1_R1 = QLabel(self)
        lb1_R2 = QLabel(self)
        lb1_R3 = QLabel(self)
        lb1_R4 = QLabel(self)
        lb1_R5 = QLabel(self)
        lb1_R6 = QLabel(self)
        lb1_R7 = QLabel(self)
        lb1_R8 = QLabel(self)
        lb1_R9 = QLabel(self)
        lb1_R10 = QLabel(self)
        lb1_R11 = QLabel(self)
        lb1_R12 = QLabel(self)
        lb1_R13 = QLabel(self)

        lb1_R1.setText(f"R1(in million): {config.R1}")
        lb1_R2.setText(f"R2(in bytes): {config.R2}")
        lb1_R3.setText(f"R3(in KB): {config.R3}")
        lb1_R4.setText(f"R4: {config.R4}")
        lb1_R5.setText(f"R5(in sec): {config.R5}")
        lb1_R6.setText(f"R6(in million): {config.R6}")
        lb1_R7.setText(f"R7(in bytes): {config.R7}")
        lb1_R8.setText(f"R8(in KB): {config.R8}")
        lb1_R9.setText(f"R9: {config.R9}")
        lb1_R10.setText(f"R10: {config.R10}")
        lb1_R11.setText(f"R11(Ratio T1/T2) : {config.R3/config.R8}")
        lb1_R12.setText(f"R12_T1: {config.R12_T1}")
        lb1_R13.setText(f"R12_T2: {config.R12_T2}")


        lb1_R1.setAlignment(Qt.AlignLeft)
        lb1_R2.setAlignment(Qt.AlignLeft)
        lb1_R3.setAlignment(Qt.AlignLeft)
        lb1_R4.setAlignment(Qt.AlignLeft)
        lb1_R5.setAlignment(Qt.AlignLeft)
        lb1_R6.setAlignment(Qt.AlignLeft)
        lb1_R7.setAlignment(Qt.AlignLeft)
        lb1_R8.setAlignment(Qt.AlignLeft)
        lb1_R9.setAlignment(Qt.AlignLeft)
        lb1_R10.setAlignment(Qt.AlignLeft)
        lb1_R11.setAlignment(Qt.AlignLeft)
        lb1_R12.setAlignment(Qt.AlignLeft)
        lb1_R13.setAlignment(Qt.AlignLeft)


        left.addWidget(lb1_R1)


        left.addWidget(lb1_R2)
        left.addWidget(lb1_R3)
        left.addWidget(lb1_R4)
        left.addWidget(lb1_R5)
        left.addWidget(lb1_R6)
        left.addWidget(lb1_R7)
        left.addWidget(lb1_R8)
        left.addWidget(lb1_R9)
        left.addWidget(lb1_R10)
        left.addWidget(lb1_R11)
        left.addWidget(lb1_R12)
        left.addWidget(lb1_R13)



        hbox.setAlignment(Qt.AlignLeft)
        hbox.addLayout(left, 1)

        self.ball_bfs = Ball(self)

        self.ball_bfs.pos = QPointF(495, 35)

        self.ball_idfs = Ball(self)

        self.ball_idfs.pos = QPointF(953, 35)

        self.path_bfs = QPainterPath()

        coords_x_bfs, coords_y_bfs = self.path_to_coords(self.action_path_bfs, 450)
        coords_x_idfs, coords_y_idfs = self.path_to_coords(self.action_path_idfs, 908)

        print(coords_x_bfs, coords_y_bfs)

        self.path_bfs = QPainterPath()
        self.path_bfs.moveTo(495, 35)
        #self.path_bfs.setPen(QColor(0xff0000))
        self.path_idfs = QPainterPath()
        #self.path_idfs.setPen(QColor(0xff0000))
        self.path_idfs.moveTo(953, 35)
        for coords_x_1, coords_y_1, coords_x_2, coords_y_2 in zip(coords_x_bfs, coords_y_bfs, coords_x_idfs, coords_y_idfs):
            #print(coords_x_1, coords_y_1)
            #self.path_bfs.moveTo(coords_x, coords_y)
            self.path_bfs.lineTo(coords_x_1,  coords_y_1)
            self.path_idfs.lineTo(coords_x_2, coords_y_2)

        m = PlotCanvas(self, width = 5, height = 4)
        m.move(908, 458)

        g3 = PlotCanvas_g3(self, width = 5, height = 4)
        g3.move(450, 458)

        self.show()







    def center(self):

        qr = self.frameGeometry()
        cp  = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def drawRectangles(self, qp, x, y, width, height, color):

        qp.setBrush(QColor(color))
        qp.drawRect(x, y, width, height)

    def drawVacuum(self, qp, x, y):

        qp.setBrush(Qt.yellow)

        qp.drawEllipse(x + 45, y + 45, 10, 10 )

    def initAnimation_bfs(self):


        self.anim1 = QPropertyAnimation(self.ball_bfs, b'pos')
        self.anim1.setDuration(7000)



        self.anim1.setStartValue(QPointF(495, 35))

        vals = [p/100 for p in range(0, 101)]

        for i in vals:
            self.anim1.setKeyValueAt(i, self.path_bfs.pointAtPercent(i))

        self.anim1.setEndValue(QPointF(855, 405))


        self.anim2 = QPropertyAnimation(self.ball_idfs, b'pos')
        self.anim2.setDuration(7000)



        self.anim2.setStartValue(QPointF(953, 35))

        vals = [p/100 for p in range(0, 101)]

        for i in vals:
            self.anim2.setKeyValueAt(i, self.path_idfs.pointAtPercent(i))

        self.anim2.setEndValue(QPointF(1313, 405))


        #self.anim2.start()

        self.group = QSequentialAnimationGroup()

        self.group.addAnimation(self.anim1)
        self.group.addAnimation(self.anim2)

        self.group.start()


        #self.anim.start()

    def initAnimation_idfs(self):


        self.anim = QPropertyAnimation(self.ball_idfs, b'pos')
        self.anim.setDuration(7000)



        self.anim.setStartValue(QPointF(908, 35))

        vals = [p/100 for p in range(0, 101)]

        for i in vals:
            self.anim.setKeyValueAt(i, self.path_idfs.pointAtPercent(i))

        self.anim.setEndValue(QPointF(1268, 415))


        self.anim.start()



    def path_to_coords(self, action_list, offset):

        coords_x = []
        coords_y = []
        init_x = offset + self.state.pos_x + 45
        init_y = self.state.pos_y + 35
        #coords_x.append(init_x)
        #coords_y.append(init_y)

        for action in action_list:

            if action == "mr":
                init_x = init_x + 90
                coords_x.append(init_x)
                coords_y.append(init_y)

            elif action == "md":
                init_y = init_y + 90
                coords_x.append(init_x)
                coords_y.append(init_y)

            elif action == "ml":
                init_x = init_x - 90
                coords_x.append(init_x)
                coords_y.append(init_y)

            elif action == "mu":
                init_y = init_y - 90
                coords_x.append(init_x)
                coords_y.append(init_y)

            else:
                coords_x.append(init_x)
                coords_y.append(init_y)



        return coords_x, coords_y






"""
app = QApplication(sys.argv)
ex = AI_Vacuum()
sys.exit(app.exec_())
"""
