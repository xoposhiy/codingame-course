from state import State, Move
from simulation_task import State as StudentState
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class Visualizer(QWidget):
    checkPointRadius = 600
    buttons_size = (100, 50)
    info_block_width = 150
    viz_field_width = -1
    viz_field_height = -1
    viz_edge_empty_space = 300
    game_field_width = 16000
    game_field_height = 9000

    def __init__(self, app, viz_state: State, next_move_func,
                 laps_number=1, heuristic_number=1, is_simulation_mode=False):
        super().__init__()
        self.next_move_btn = QPushButton('Next move', self)
        self.next_move_btn.clicked.connect(self.drawNextMove)
        self.next_move_btn.setFixedSize(*self.buttons_size)

        self.prev_state_btn = QPushButton('Previous state', self)
        self.prev_state_btn.clicked.connect(self.drawPreviousState)
        self.prev_state_btn.setFixedSize(*self.buttons_size)
        self.prev_state_btn.move(0, 50)

        self.prev_state_btn.setDisabled(True)
        self.play_game_btn = QPushButton('Play game', self)
        self.play_game_btn.clicked.connect(self.drawAllGame)
        self.play_game_btn.setFixedSize(*self.buttons_size)
        self.play_game_btn.move(0, 100)

        self.state_count_label = QLabel("Move -----", self)
        self.state_count_label.move(25, 200)

        self.current_pos = QLabel(f"Car: ({viz_state.x}, {viz_state.y})", self)
        self.current_pos.move(25, 300)

        self.current_cp_number = QLabel(f"Current cp: {viz_state.checkpoint_index % len(viz_state.checkpoints)}", self)
        self.current_cp_number.move(25, 400)

        self.test_result = QLabel(f"Test_passed", self)
        self.test_result.move(25, 500)
        self.test_result.setVisible(False)

        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.resize(width-100, height-100)
        self.viz_field_width = width - 100 - self.viz_edge_empty_space - self.info_block_width
        self.viz_field_height = height - 100 - self.viz_edge_empty_space

        self.state = viz_state
        self.next_move_func = next_move_func
        self.is_simulation_mode = is_simulation_mode
        self.heuristic_number = heuristic_number
        self.laps_number = laps_number
        # best_moves = []
        # with open('BestMoves', 'r') as f:
        #     lines = f.readlines()
        # for line in lines:
        #     best_moves.append(parse_move(line))

        self.show_ghost = False

        # self.best_moves = best_moves
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
        QTimer.singleShot(60000, self.stopDrawing)

    def stopDrawing(self):
        self.picktimer.stop()

    def drawNextMove(self):
        self.prev_state_btn.setDisabled(False)
        if self.state.checkpoint_index >= self.laps_number * len(self.state.checkpoints):
            self.test_result.setVisible(True)
            self.stopDrawing
            return

        if self.is_simulation_mode:
            self.state.next_moves = self.next_move_func(StudentState(
                self.state.checkpoints, self.state.checkpoint_index,
                self.state.x, self.state.y,
                self.state.vx, self.state.vy,
                self.state.angle))
        else:
            if self.heuristic_number == 1:
                self.state.next_moves = [parse_move(self.next_move_func(self.state.next_checkpoint()))]
            if self.heuristic_number == 2:
                self.state.next_moves = [parse_move(self.next_move_func(self.state.next_checkpoint(),
                                                                    self.state.x, self.state.y, self.state.angle))]
        self.state = self.state.simulate()
        self.state_count_label.setText(f"Move {self.state.state_index}")
        self.current_pos.setText(f"Car: ({self.state.x}, {self.state.y})")
        self.current_cp_number.setText(f"Current cp: {self.state.checkpoint_index % len(self.state.checkpoints)}")
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
        self.drawPath(qp)
        self.drawAimPoint(qp)
        if self.show_ghost:
            self.drawGhost(qp)
        qp.end()

    def drawCheckpoints(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for index, checkpoint in enumerate(self.state.checkpoints):
            qp.drawText(self.normalize_x(checkpoint[0] - 50), self.normalize_y(checkpoint[1] + 100), str(index))
            qp.drawEllipse(self.normalize_x(checkpoint[0] - self.checkPointRadius), self.normalize_y(checkpoint[1] - self.checkPointRadius),
                           self.normalize_raduis_x(2*self.checkPointRadius), self.normalize_raduis_y(2*self.checkPointRadius))

    def drawCar(self, qp):
        pen = QPen(Qt.black, 6, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawPoint(self.normalize_x(self.state.x), self.normalize_y(self.state.y))

    def drawSpeedVector(self, qp):
        pen = QPen(Qt.darkYellow, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.normalize_x(self.state.x), self.normalize_y(self.state.y),
                    self.normalize_x(self.state.x + self.state.vx), self.normalize_y(self.state.y + self.state.vy))

    def drawPath(self, qp):
        pen = QPen(Qt.blue, 2, Qt.SolidLine)
        qp.setPen(pen)
        if len(self.state.passed_points) == 0:
            return
        prev_point = self.state.passed_points[0]
        for point in self.state.passed_points[1:]:
            qp.drawLine(self.normalize_x(prev_point[0]), self.normalize_y(prev_point[1]),
                    self.normalize_x(point[0]), self.normalize_y(point[1]))
            prev_point = point
        qp.drawLine(self.normalize_x(prev_point[0]), self.normalize_y(prev_point[1]),
                    self.normalize_x(self.state.x), self.normalize_y(self.state.y))

    def drawAimPoint(self, qp):
        pen = QPen(Qt.red, 2, Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(self.normalize_x(self.state.x), self.normalize_y(self.state.y),
                    self.normalize_x(self.state.next_moves[0].x), self.normalize_y(self.state.next_moves[0].y))

    def drawTrajectory(self, qp):
        pen = QPen(Qt.green, 3, Qt.SolidLine)
        qp.setPen(pen)
        state_copy = self.state.copy()
        for move in self.state.next_moves:
            cur_x, cur_y = state_copy.x, state_copy.y
            state_copy.simulate_move(move)
            qp.drawLine(self.normalize_x(cur_x), self.normalize_y(cur_y),
                    self.normalize_x(state_copy.x), self.normalize_y(state_copy.y))

    def normalize_x(self, value: int):
        return (value * self.viz_field_width) // self.game_field_width + self.info_block_width + self.viz_edge_empty_space//2

    def normalize_y(self, value: int):
        return (value * self.viz_field_height) // self.game_field_height + self.viz_edge_empty_space//2

    def normalize_raduis_x(self, value: int):
        return (value * self.viz_field_width) // self.game_field_width

    def normalize_raduis_y(self, value: int):
        return (value * self.viz_field_width) // self.game_field_width

