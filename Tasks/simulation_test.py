import sys
import pytest
import unittest
from visualizer import Visualizer
from simulation_task import *
from state import State

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

Visualize = True


class SimulationTests(unittest.TestCase):

    def test_basic(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        timer = QTimer()

        if (Visualize):
            app = QApplication([])
            visualizer = Visualizer(s, random_search, True)
            visualizer.setWindowTitle("test_sim")
            visualizer.show()

            # visualizer.drawAllGame()

            app.exec()
