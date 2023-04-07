import sys
import math
from state import State, Move
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer

NormScale = 8


def Normalize(value: int):
    return value // NormScale


class Visualizer(QWidget):
    checkPointRadius = 600

    def __init__(self, viz_state: State, next_move_func):
        super().__init__()
        next_move_btn = QPushButton('Next move', self)
        next_move_btn.clicked.connect(self.drawNextMove)
        play_game_btn = QPushButton('Play game', self)
        play_game_btn.clicked.connect(self.drawAllGame)
        play_game_btn.move(0, 70)

        # self.setGeometry(50,50, 5000, 2000)
        # x = self.width()
        # y = self.height()
        self.showMaximized()

        #посмотреть зум контрол
        # x = self.width()
        # y = self.height()
        self.State = viz_state
        self.next_move_func = next_move_func
        self.picktimer = QTimer()

    def drawAllGame(self):
        self.picktimer.setInterval(100)
        self.picktimer.timeout.connect(self.drawNextMove)
        self.picktimer.start()
        QTimer.singleShot(5000, self.stopDrawing)

    def stopDrawing(self):
        self.picktimer.stop()

    def drawNextMove(self):
        self.State.next_moves = [self.next_move_func(self.State.next_checkpoint())]
        self.State.simulate()
        self.update()

    def paintEvent(self, e):
        self.drawState()

    def drawState(self):
        qp = QPainter()
        qp.begin(self)
        self.drawCheckpoints(qp)
        self.drawCar(qp)
        self.drawSpeedVector(qp)
        qp.end()

    def drawCheckpoints(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for checkpoint in self.State.checkpoints:
            qp.drawEllipse(Normalize(checkpoint[0] - 300), Normalize(checkpoint[1] - 300),
                           Normalize(self.checkPointRadius), Normalize(self.checkPointRadius))

    def drawCar(self, qp):
        pen = QPen(Qt.black, 6, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawPoint(Normalize(self.State.x), Normalize(self.State.y))

    def drawSpeedVector(self, qp):
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(Normalize(self.State.x), Normalize(self.State.y),
                    Normalize(self.State.x + self.State.vx), Normalize(self.State.y + self.State.vy))

