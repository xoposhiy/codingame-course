import unittest
from visualizer import Visualizer
from heuristic import heuristic
from visualizer_state import State, Move

from PyQt5.QtWidgets import QApplication

unittest.TestLoader.sortTestMethodsUsing = None

Visualize = True


def parse_move(line: str):
    parts = line.split(" ")
    return Move(int(parts[0]), int(parts[1]), int(parts[2]))


class HeuristicTests(unittest.TestCase):
    def test_two_points(self):
        chs = [(2000, 2000), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 2
        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(app, s, heuristic, laps_number=laps_number, heuristic_number=1)
            visualizer.setWindowTitle("test_two_points")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints)*laps_number)

    def test_zig_zag(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        state = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turn_number = 0
        laps_number = 1

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, state, heuristic, laps_number=laps_number)
            visualizer.setWindowTitle("test_zig_zag")
            visualizer.show()
            app.exec()
        else:
            while turn_number < 600:
                state.simulate_move(parse_move(heuristic(state.next_checkpoint())))
                turn_number += 1
            self.assertGreaterEqual(state.checkpoint_index, len(state.checkpoints) * laps_number)

    def test_half_round_and_round(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 86, [], [])
        turn_number = 0
        laps_number = 1

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(app, s, heuristic, laps_number=laps_number, heuristic_number=1)
            visualizer.setWindowTitle("test_half_round_and_round")
            visualizer.show()
            # visualizer.drawAllGame()
            app.exec()
        else:
            while turn_number < 600:
                s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
                turn_number += 1
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)
