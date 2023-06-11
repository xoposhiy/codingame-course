from state import State, Move
from simulation_task import State as StudentState
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt, QTimer


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class Visualizer(QWidget):
    checkPointRadius = 600
    buttons_size = (120, 50)
    info_block_width = 250
    viz_field_width = -1
    viz_field_height = -1
    viz_edge_empty_space = 450
    game_field_width = 16000
    game_field_height = 9000
    border_delta = 100

    def __init__(self, app, viz_state: State, next_move_func,
                 laps_number=1, heuristic_number=1, is_simulation_mode=False):
        super().__init__()
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()

        self.show_path = True
        self.show_speed = True
        self.show_trajectories = True
        self.show_aim = True

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

        font = QFont("Times", 12)

        self.init_labels(25, 25, 65, self.info_block_width + self.viz_edge_empty_space, width, font)

        self.init_checkboxes(25, 320, 30, font)

        self.init_buttons(25, 500, 100)

        if self.show_path:
            self.show_path_cb.toggle()
        if self.show_trajectories:
            self.show_trajectories_cb.toggle()
        if self.show_aim:
            self.show_aim_cb.toggle()
        if self.show_speed:
            self.show_speed_cb.toggle()

        self.resize(width-self.border_delta, height-self.border_delta)
        self.viz_field_width = width - self.border_delta - self.viz_edge_empty_space - self.info_block_width
        self.viz_field_height = height - self.border_delta - self.viz_edge_empty_space

        # self.best_moves = best_moves
        self.picktimer = QTimer()

    # noinspection PyAttributeOutsideInit
    def init_labels(self, start_x, start_y, delta_y, max_label_width, width_for_result, font):
        state = self.state
        cur_x, cur_y = start_x, start_y

        self.state_count_label = self.init_label(cur_x, cur_y, "Ход: 0", max_label_width, font)
        cur_y += delta_y - 30

        self.car_pos_label = self.init_label(cur_x, cur_y,
                                             f"Координаты машинки\n x: {state.x}, y: {state.y}",
                                             max_label_width, font)
        cur_y += delta_y

        self.car_speed_label = self.init_label(cur_x, cur_y,
                                               f"Скорость машинки\n vx: {state.vx}, vy: {state.vy}",
                                               max_label_width, font)
        cur_y += delta_y

        self.car_angle_label = self.init_label(cur_x, cur_y, f"Угол машинки\n angle: {state.angle}",
                                               max_label_width, font)
        cur_y += delta_y

        cp_number = state.checkpoint_index % len(state.checkpoints)
        cp = state.next_checkpoint()
        self.current_cp_label = self.init_label(cur_x, cur_y,
                                                f"Следующий чекпоинт \nномер: {cp_number}, cp_x: {cp[0]}, cp_y: {cp[1]}",
                                                max_label_width, font)

        self.test_result = self.init_label((width_for_result - self.border_delta) // 2, 50,
                                           "Тест пройден!",
                                           max_label_width, QFont("Times", 18))
        self.test_result.setVisible(False)

    def init_label(self, x, y, text, max_label_width, font):
        label = QLabel(text, self)
        label.setMaximumWidth(max_label_width)
        label.move(x, y)
        label.setFont(font)
        return label

    # noinspection PyAttributeOutsideInit
    def init_checkboxes(self, start_x, start_y, delta_y, font):
        cur_x, cur_y = start_x, start_y

        self.show_path_cb = self.init_checkbox(cur_x, cur_y, "Показывать пройденный путь", font, self.path_cb_change)
        cur_y += delta_y

        self.show_speed_cb = self.init_checkbox(cur_x, cur_y, "Показывать вектор скорости", font, self.speed_cb_change)
        cur_y += delta_y

        self.show_aim_cb = self.init_checkbox(cur_x, cur_y, "Показывать точку хода", font, self.aim_cb_change)
        cur_y += delta_y

        self.show_trajectories_cb = self.init_checkbox(cur_x, cur_y, "Показывать возможные траектории",
                                                       font, self.trajectories_cb_change)

    def init_checkbox(self, x, y, text, font, function):
        cb = QCheckBox(text, self)
        cb.setFont(font)
        cb.move(x, y)
        cb.stateChanged.connect(function)
        return cb

    # noinspection PyAttributeOutsideInit
    def init_buttons(self, start_x, start_y, delta_y):
        cur_x, cur_y = start_x, start_y

        self.prev_state_btn = self.init_button(cur_x, cur_y, "Откатить ход", self.draw_previous_state)
        self.prev_state_btn.setDisabled(True)
        cur_y += delta_y

        self.next_move_btn = self.init_button(cur_x, cur_y, "Следующий ход", self.draw_next_move)
        cur_y += delta_y

        self.play_game_btn = self.init_button(cur_x, cur_y, "Воспроизвести", self.draw_all_game)

        self.pause_game_btn = self.init_button(cur_x, cur_y, "Пауза", self.stop_drawing)
        self.pause_game_btn.setVisible(False)

    def init_button(self, x, y, text, function):
        button = QPushButton(text, self)
        button.clicked.connect(function)
        button.setFixedSize(*self.buttons_size)
        button.move(x, y)
        return button

    def draw_previous_state(self):
        self.test_result.setVisible(False)
        self.play_game_btn.setDisabled(False)
        self.state = self.state.previous_state
        self.update_labels()
        if self.state.previous_state is None:
            self.prev_state_btn.setDisabled(True)
        self.update()

    def draw_all_game(self):
        self.picktimer = QTimer()
        self.picktimer.setInterval(100)
        self.picktimer.timeout.connect(self.draw_next_move)
        self.picktimer.start()
        self.pause_game_btn.setVisible(True)
        self.play_game_btn.setVisible(False)
        QTimer.singleShot(60000, self.stop_drawing)

    def stop_drawing(self):
        self.picktimer.stop()
        self.pause_game_btn.setVisible(False)
        self.play_game_btn.setVisible(True)
        if self.state.checkpoint_index < self.laps_number * len(self.state.checkpoints):
            self.play_game_btn.setDisabled(False)

    def draw_next_move(self):
        self.prev_state_btn.setDisabled(False)
        if self.state.checkpoint_index >= self.laps_number * len(self.state.checkpoints):
            self.play_game_btn.setDisabled(True)
            self.test_result.setVisible(True)
            self.stop_drawing()
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
        self.update_labels()
        self.update()

    def path_cb_change(self, state):
        self.show_path = state == Qt.Checked
        self.update()

    def speed_cb_change(self, state):
        self.show_speed = state == Qt.Checked
        self.update()

    def trajectories_cb_change(self, state):
        self.show_trajectories = state == Qt.Checked
        self.update()

    def aim_cb_change(self, state):
        self.show_aim = state == Qt.Checked
        self.update()

    def update_labels(self):
        self.state_count_label.setText(f"Ход: {self.state.state_index}")
        self.car_pos_label.setText(f"Координаты машинки\n x: {self.state.x}, y: {self.state.y}")
        cp_number = self.state.checkpoint_index % len(self.state.checkpoints)
        cp = self.state.next_checkpoint()
        self.current_cp_label.setText(f"Следующий чекпоинт \n"
                                      f"номер: {cp_number}, cp_x: {cp[0]}, cp_y: {cp[1]}")
        self.car_speed_label.setText(f"Скорость машинки\n vx: {self.state.vx}, vy: {self.state.vy}")
        self.car_angle_label.setText(f"Угол машинки\n angle: {self.state.angle}")

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
        if self.show_speed:
            self.drawSpeedVector(qp)
        if self.show_trajectories:
            self.drawTrajectories(qp)
        if self.show_path:
            self.drawPath(qp)
        if self.show_aim:
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
        if len(self.state.next_moves) != 0:
            qp.drawLine(self.normalize_x(self.state.x), self.normalize_y(self.state.y),
                    self.normalize_x(self.state.next_moves[0].x), self.normalize_y(self.state.next_moves[0].y))

    def drawTrajectories(self, qp):
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

