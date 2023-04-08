import sys
import pytest
import unittest
from heuristic_initial import *
from state import State

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

Visualize = True


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class HeuristicTests(unittest.TestCase):
    def test_basic(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        timer = QTimer()


if __name__ == '__main__':
    unittest.main()