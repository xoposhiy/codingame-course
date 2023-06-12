import unittest
from samegame import *
from PyQt5.QtWidgets import QApplication
from visualizer import Visualizer

Visualize = True

class GreedyTests(unittest.TestCase):
    def test_1(self):
        s = read_state_from([
            '1 1 2',
            '2 3 4'])

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, greedy_ai, estimate)
            visualizer.setWindowTitle("final_test")
            visualizer.show()
            app.exec()
        else:
            moves = solve(state)
            print(moves)
            for m in moves:
                state = state.apply_move(m)
            print(state.score)

    def test_2(self):
        s = read_state_from([
            '2 2 1',
            '1 1 3',
            '1 2 3'])

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, greedy_ai, estimate)
            visualizer.setWindowTitle("final_test")
            visualizer.show()
            app.exec()
        else:
            moves = solve(state)
            print(moves)
            for m in moves:
                state = state.apply_move(m)
            print(state.score)

    def test_3(self):
        s = read_state_from([
            '2 1 1 4 1',
            '1 2 1 4 1',
            '1 1 1 4 4',
            '1 2 1 4 4',
            '1 1 2 4 3'])
        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, greedy_ai, estimate)
            visualizer.setWindowTitle("final_test")
            visualizer.show()
            app.exec()
        else:
            moves = solve(state)
            print(moves)
            for m in moves:
                state = state.apply_move(m)
            print(state.score)

    def test_4(self):
        s = read_state_from(
            '3 1 1 4 1 0 4 0 4 4 1 1 0 2 3\n'
            '3 3 2 0 4 4 1 3 1 2 0 0 4 0 4\n'
            '0 2 3 4 3 0 3 0 0 3 4 4 1 1 1\n'
            '2 3 4 0 2 3 0 2 4 4 4 3 0 2 3\n'
            '1 2 1 3 1 2 0 1 2 1 0 3 4 0 1\n'
            '0 4 4 3 0 3 4 2 2 2 0 2 3 4 0\n'
            '2 4 3 4 2 3 1 1 1 3 4 1 0 3 1\n'
            '1 0 0 4 0 3 1 2 1 0 4 1 3 3 1\n'
            '1 3 3 2 0 4 3 1 3 0 4 1 0 0 3\n'
            '0 3 3 4 2 3 0 0 2 1 2 3 4 0 1\n'
            '0 4 1 2 0 1 3 4 3 3 4 1 4 0 4\n'
            '2 2 3 1 0 4 0 1 2 4 1 3 3 0 1\n'
            '3 3 0 2 3 2 1 4 3 1 3 0 2 1 3\n'
            '1 0 3 2 1 4 4 4 4 0 4 2 1 3 4\n'
            '1 0 1 0 1 1 2 2 1 0 0 1 4 3 2'
                .splitlines())

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, greedy_ai, estimate)
            visualizer.setWindowTitle("final_test")
            visualizer.show()
            app.exec()
        else:
            moves = solve(state)
            print(moves)
            for m in moves:
                state = state.apply_move(m)
            print(state.score)

    def test_ulearn(self):
        s = read_state_from(
            '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 0 4 0 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 0 4 0 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 0 4 0 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 0 4 0 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 0 0 4 0 4 4 4 4 4 4\n'
            '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n'
            '3 4 4 2 2 2 4 1 4 3 3 4 1 4 1\n'
            '3 4 4 2 4 4 1 4 1 3 4 3 1 4 1\n'
            '3 4 4 2 2 2 1 1 1 3 3 4 1 1 1\n'
            '3 4 3 2 4 4 1 4 1 3 4 3 1 4 1\n'
            '3 3 3 2 2 2 1 4 1 3 4 3 1 4 1\n'
            '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n'
            '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4'
                .splitlines())

        if Visualize:
            app = QApplication([])
            visualizer = Visualizer(app, s, greedy_ai, estimate)
            visualizer.setWindowTitle("final_test")
            visualizer.show()
            app.exec()
        else:
            moves = solve(state)
            print(moves)
            for m in moves:
                state = state.apply_move(m)
            print(state.score)