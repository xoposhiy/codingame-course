import unittest
import cProfile
from samegame import *


class MovesTests(unittest.TestCase):
    def test_moves_are_empty(self):
        s = read_state_from([
            '1 2 1 2',
            '2 1 2 1'])
        moves = list(s.moves())
        assert moves == []


    def test_moves_single_move(self):
        s = read_state_from([
            '1 1 2',
            '2 3 4'])
        moves = list(s.moves())
        assert len(moves) == 1
        assert moves[0] == [(0, 1), (1, 1)]


    def test_moves_many_moves(self):
        s = read_state_from([
            '1 1 1 3',
            '2 2 4 3'])
        moves = [sorted(m) for m in s.moves()]
        assert len(moves) == 3
        assert [(0, 0), (1, 0)] in moves
        assert [(0, 1), (1, 1), (2, 1)] in moves
        assert [(3, 0), (3, 1)] in moves


    def test_moves_one_large_area(self):
        s = read_state_from([
            '1 1',
            '1 1'])
        moves = [sorted(m) for m in s.moves()]
        assert len(moves) == 1
        assert [(0, 0), (0, 1), (1, 0), (1, 1)] in moves


    def test_moves_large_area(self):
        s = read_state_from([
            '2 1 1 4 1',
            '1 2 1 4 1',
            '1 1 1 4 4',
            '1 2 1 4 4',
            '1 1 2 4 3'])
        moves = [sorted(m) for m in s.moves()]
        assert len(moves) == 3
        assert [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4)] in moves
        assert [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), ] in moves
        assert [(4, 3), (4, 4)] in moves
