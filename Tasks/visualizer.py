import sys
import math
from state import State, Move
from simulation_task import State as StudentState
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer

NormScale = 8


def Normalize(value: int):
    return value // NormScale


class Visualizer(QWidget):
    checkPointRadius = 600

    def __init__(self, viz_state: State, next_move_func, is_simulation_mode=False):
        super().__init__()
        self.next_move_btn = QPushButton('Next move', self)
        self.next_move_btn.clicked.connect(self.drawNextMove)
        self.prev_state_btn = QPushButton('Previous state', self)
        self.prev_state_btn.clicked.connect(self.drawPreviousState)
        self.prev_state_btn.move(0, 50)
        self.prev_state_btn.setDisabled(True)
        self.play_game_btn = QPushButton('Play game', self)
        self.play_game_btn.clicked.connect(self.drawAllGame)
        self.play_game_btn.move(0, 100)

        self.state_count_label = QLabel("Move 0", self)
        self.state_count_label.move(200, 50)

        # self.setGeometry(50,50, 5000, 2000)
        # x = self.width()
        # y = self.height()
        self.showMaximized()

        #посмотреть зум контрол
        # x = self.width()
        # y = self.height()
        self.state = viz_state
        self.next_move_func = next_move_func
        self.is_simulation_mode = is_simulation_mode
        self.picktimer = QTimer()

    def drawPreviousState(self):
        self.state = self.state.previous_state
        self.state_count_label.setText(f"Move {self.state.state_index}")
        if self.state.previous_state is None:
            self.prev_state_btn.setDisabled(True)
        self.update()

    def drawAllGame(self):
        self.picktimer.setInterval(100)
        self.picktimer.timeout.connect(self.drawNextMove)
        self.picktimer.start()
        QTimer.singleShot(5000, self.stopDrawing)

    def stopDrawing(self):
        self.picktimer.stop()

    def drawNextMove(self):
        self.prev_state_btn.setDisabled(False)

        # if self.state.next_state is not None:
        #     self.state = self.state.next_state
        #     self.update()
        #     return

        if self.is_simulation_mode:
            self.state.next_moves = self.next_move_func(StudentState(
                self.state.checkpoints, self.state.checkpoint_index,
                self.state.x, self.state.y,
                self.state.vx, self.state.vy,
                self.state.angle))
        else:
            self.state.next_moves = [self.next_move_func(self.state.next_checkpoint())]
        self.state = self.state.simulate()
        self.state_count_label.setText(f"Move {self.state.state_index}")
        self.update()

    def paintEvent(self, e):
        self.drawState()

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.RightArrow:
    #         self.drawNextMove()
    #     if e.key() == Qt.LeftArrow:
    #         self.drawPreviousState()
    #     if e.key() == Qt.Key_Space:
    #         self.drawAllGame()

    def drawState(self):
        qp = QPainter()
        qp.begin(self)
        self.drawCheckpoints(qp)
        self.drawCar(qp)
        self.drawSpeedVector(qp)
        self.drawTrajectory(qp)
        qp.end()

    def drawCheckpoints(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for checkpoint in self.state.checkpoints:
            qp.drawEllipse(Normalize(checkpoint[0] - 300), Normalize(checkpoint[1] - 300),
                           Normalize(self.checkPointRadius), Normalize(self.checkPointRadius))

    def drawCar(self, qp):
        pen = QPen(Qt.black, 6, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawPoint(Normalize(self.state.x), Normalize(self.state.y))

    def drawSpeedVector(self, qp):
        pen = QPen(Qt.green, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(Normalize(self.state.x), Normalize(self.state.y),
                    Normalize(self.state.x + self.state.vx), Normalize(self.state.y + self.state.vy))

    def drawTrajectory(self, qp):
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        state_copy = self.state.copy()
        for move in self.state.next_moves:
            cur_x, cur_y = state_copy.x, state_copy.y
            state_copy.simulate_move(move)
            qp.drawLine(Normalize(cur_x), Normalize(cur_y),
                    Normalize(state_copy.x), Normalize(state_copy.y))
