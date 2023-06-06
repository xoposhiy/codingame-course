import sys
import pytest
import unittest
from visualizer import Visualizer
from heuristic_task import *
from state import State

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

Visualize = False


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class HeuristicTests(unittest.TestCase):

    def test_heruisic1(self):
        chs = [(7000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(s, heuristic)
            visualizer.setWindowTitle("test")
            visualizer.show()
            # visualizer.drawAllGame()
            app.exec()
        else:
            while turnNumber < 600:
                s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
                turnNumber += 1
                if s.checkpoint_index == len(s.checkpoints):
                    break
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints))

    def test_heruisic11(self):
        chs = [(7000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(s, heuristic)
            visualizer.setWindowTitle("test")
            visualizer.show()
            # visualizer.drawAllGame()
            app.exec()
        else:
            while turnNumber < 600:
                s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
                turnNumber += 1
                if s.checkpoint_index == len(s.checkpoints) * 3:
                    break
            self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * 3)


    # def test_basic_viz(self):
    #     chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
    #     s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
    #     turnNumber = 0
    #
    #     if (Visualize):
    #         app = QApplication([])
    #         visualizer = Visualizer(s, heuristic)
    #         visualizer.setWindowTitle("test")
    #         visualizer.show()
    #         # visualizer.drawAllGame()
    #         app.exec()
    #     else:
    #         while turnNumber < 600:
    #             s.simulate_move(heuristic(s.next_checkpoint()))
    #             turnNumber += 1
    #         self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * 3)


# if __name__ == "__main__":
#     unittest.main()