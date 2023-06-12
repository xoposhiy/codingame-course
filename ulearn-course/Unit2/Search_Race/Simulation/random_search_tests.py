import unittest
from visualizer import Visualizer
from visualizer_state import State
from random_search_task import random_search
from PyQt5.QtWidgets import QApplication

unittest.TestLoader.sortTestMethodsUsing = None
Visualize = True


class RandomSearchTests(unittest.TestCase):
    def test_two_points(self):
        chs = [(2000, 2000), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, random_search, laps_number=laps_number, is_simulation_mode=True)
            visualizer.setWindowTitle("test_two_points")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(random_search(s))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_zig_zag(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turn_number = 0
        laps_number = 3

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, random_search, laps_number=laps_number, is_simulation_mode=True)
            visualizer.setWindowTitle("test_zig_zag")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(random_search(s))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)


    def test_three_random(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        turn_number = 0
        laps_number = 3

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, random_search, laps_number=laps_number, is_simulation_mode=True)
            visualizer.setWindowTitle("test_three_random")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(random_search(s))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_tokio_drift(self):
        chs = [(1000, 1000), (12000, 1000), (12500, 2500), (13000, 4000),
               (12500, 5500), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, random_search, laps_number=laps_number, is_simulation_mode=True)
            visualizer.setWindowTitle("test_tokio_drift")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(random_search(s))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_round_and_round(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000),
               (8000, 7000), (7500, 5500), (7500, 2500), (8000, 1000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 72, [], [])
        turn_number = 0
        laps_number = 3

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, random_search, laps_number=laps_number, is_simulation_mode=True)
            visualizer.setWindowTitle("test_round_and_round")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(random_search(s))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_hold_the_line(self):
        chs = [(1000, 4500), (2500, 3905), (4000, 5095), (5500, 3905),
               (7000, 5095), (8500, 3905), (10000, 5095), (11500, 3905)]
        s = State(chs, 0, 1000, 4500, 0, 0, 338, [], [])
        turn_number = 0
        laps_number = 3

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, random_search, laps_number=laps_number, is_simulation_mode=True)
            visualizer.setWindowTitle("test_hold_the_line")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(random_search(s))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)
