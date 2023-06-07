import sys
import pytest
import unittest
from visualizer import Visualizer
from heuristic_task import *
from state import State, Move

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

Visualize = True


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class HeuristicTests(unittest.TestCase):
    def test_heruisic1(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000)] # (1000, 4000)]#, (3500, 5500), (3500, 2500), (4000, 1000)]

        # chs = [(8500, 1000), (10975,2025), (12000, 4500), (8500, 8000), (5000, 4500)]  # , (3500, 5500), (3500, 2500), (4000, 1000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 86, [], [])
        turnNumber = 0

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(s, heuristic, 1)
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

    def test_heruisic2(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(s, heuristic, 1)
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
