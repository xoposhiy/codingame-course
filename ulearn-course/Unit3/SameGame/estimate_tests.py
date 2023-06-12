import unittest
from samegame import *


class EstimateTests(unittest.TestCase):
    def test_apply_move(self):
        s = read_state_from([
            '1 1 2',
            '2 3 4'])
        score = estimate(s)
        assert score == 0

    def test_apply_move_fly_down(self):
        s = read_state_from([
            '2 2 1',
            '1 1 3',
            '1 2 3'])
        score = estimate(s)
        assert score == 1

    def test_apply_move_fly_down(self):
        s = read_state_from([
            '2 2 1',
            '1 1 3',
            '1 2 3'])
        s.score = 5
        score = estimate(s)
        assert score == 6

    def test_apply_move_compaction(self):
        s = read_state_from([
            '1 . 3 .',
            '2 1 1 1',
            '3 1 2 1'])
        score = estimate(s)
        assert score == 9


    def test_moves_empty_column(self):
        s = read_state_from([
            '1 1',
            '1 1'])
        score = estimate(s)
        assert score == 4


    def test_moves_large_area(self):
        s = read_state_from([
            '2 1 1 4 1',
            '1 2 1 4 1',
            '1 1 1 4 4',
            '1 2 1 4 4',
            '1 1 2 4 3'])
        s.score = 24
        score = estimate(s)
        assert score == 130

