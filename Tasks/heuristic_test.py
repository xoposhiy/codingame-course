import sys
import pytest
import unittest
from visualizer import Visualizer
from heuristic_task import *
from state import State, Move, parse_move

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

Visualize = True

# def test_heuristic():
#     assert heuristic([10000, 5000]) == "10000 5000 200"
#     assert heuristic([3358, 2838]) == "3358 2838 200"
#     assert heuristic([2757, 4659]) == "2757 4659 200"
#     assert heuristic([10353, 1986]) == "10353 1986 200"

class HeuristicTests(unittest.TestCase):

    # @classmethod
    # def setUp(self) -> None:
    #     self.
    
    def test_basic(self):
        # checkpoint_x, checkpoint_y = 300, 400
        # actual = heuristic([checkpoint_x, checkpoint_y])
        # expected = "300 400 200"
        # self.assertEqual(actual, expected)
        #
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        timer = QTimer()

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(s)
            visualizer.setWindowTitle("test")
            visualizer.show()
            # timer.start(1000)

            # k = 0
            # while k < 1000:
            #     if not timer.isActive():
            #         visualizer.State.next_moves = [
            #             parse_move(heuristic(visualizer.State.checkpoints[visualizer.State.checkpoint_index]))]
            #         visualizer.State.simulate()
            #         visualizer.update()
            #         k += 1
            #         timer.restart()

            for i in range(1000):
                visualizer.State.next_moves = [parse_move(heuristic(visualizer.State.next_checkpoint()))]
                visualizer.State.simulate()
                visualizer.update()

            app.exec()
