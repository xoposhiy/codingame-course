from samegame import State
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush
from PyQt5.QtCore import Qt, QTimer


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

    def __init__(self, app, viz_state: State, next_move_func, estimate_func):
        super().__init__()
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()

        # self.show_path = True
        # self.show_speed = True
        # self.show_trajectories = True
        # self.show_aim = True

        self.state = viz_state
        self.max_width = len(viz_state.columns)
        self.max_height = len(viz_state.columns[0])
        self.cur_width = len(viz_state.columns)
        self.cur_height = len(viz_state.columns)
        self.next_move_func = next_move_func
        self.estimate_func = estimate_func

        font = QFont("Times", 12)

        self.init_labels(50, 150, 65, self.info_block_width + self.viz_edge_empty_space, width, font)

        self.init_buttons(50, 300, 100)

        self.resize(width-self.border_delta, height-self.border_delta)
        self.viz_field_width = width - self.border_delta - self.viz_edge_empty_space - self.info_block_width
        self.viz_field_height = height - self.border_delta - self.viz_edge_empty_space

        # self.best_moves = best_moves
        self.picktimer = QTimer()

    # noinspection PyAttributeOutsideInit
    def init_labels(self, start_x, start_y, delta_y, max_label_width, width_for_result, font):
        state = self.state
        cur_x, cur_y = start_x, start_y

        self.state_count_label = self.init_label(cur_x, cur_y, "Ход: 0\t", max_label_width, font)
        cur_y += delta_y - 30

        self.score_label = self.init_label(cur_x, cur_y, "Счёт: 0\t", max_label_width, font)

        self.test_result = self.init_label((width_for_result - self.border_delta) // 2, 30,
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

    def draw_next_move(self):
        self.prev_state_btn.setDisabled(False)
        move = self.next_move_func(self.state, self.estimate_func)
        if move is None:
            self.play_game_btn.setDisabled(True)
            self.test_result.setVisible(True)
            self.stop_drawing()
            return

        self.state = self.state.apply_move(move)
        self.draw_state()

        self.update_labels()
        self.update()

    def draw_state(self):
        state = self.state
        cur_x = 500
        cur_y = 850
        size = 50
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for col in range(self.max_width):
            qp.drawLine(cur_x, cur_y,
                        cur_x, cur_y - size * self.max_height)
            cur_x += size
        qp.drawLine(cur_x, cur_y,
                    cur_x, cur_y - size * self.max_height)

        cur_x = 500
        cur_y = 850
        for col in range(self.max_height):
            qp.drawLine(cur_x, cur_y,
                        cur_x + size * self.max_width, cur_y)
            cur_y -= size
        qp.drawLine(cur_x, cur_y,
                    cur_x + size * self.max_width, cur_y)

        cur_x = 500
        cur_y = 850
        for col in state.columns:
            for cell in col:
                if cell == 0:
                    qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
                if cell == 1:
                    qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
                if cell == 2:
                    qp.setBrush(QBrush(Qt.green, Qt.SolidPattern))
                if cell == 3:
                    qp.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                if cell == 4:
                    qp.setBrush(QBrush(Qt.darkMagenta, Qt.SolidPattern))
                qp.drawRect(cur_x, cur_y - size,
                            size,size)
                cur_y -= size
            cur_x += size
            cur_y = 850
        qp.end()


    def update_labels(self):
        self.state_count_label.setText(f"Ход: {self.state.turn_number}")
        self.score_label.setText(f"Счёт: {self.state.score}")

    def paintEvent(self, e):
        self.draw_state()

