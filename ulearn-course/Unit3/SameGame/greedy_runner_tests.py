import unittest
from samegame import *


# noinspection PyMethodMayBeStatic
class GreedyTests(unittest.TestCase):
    def test_1(self):
        state = read_state_from([
            '1 1 2',
            '2 3 4'])
        moves = solve(state)
        for m in moves:
            state = state.apply_move(m)
        assert state.score == 0

    def test_2(self):
        state = read_state_from([
            '2 2 1',
            '1 1 3',
            '1 2 3'])

        moves = solve(state)
        for m in moves:
            state = state.apply_move(m)
        assert state.score == 2

    def test_medium_field(self):
        state = read_state_from([
            '2 1 1 4 1',
            '1 2 1 4 1',
            '1 1 1 4 4',
            '1 2 1 4 4',
            '1 1 2 4 3'])
        moves = solve(state)
        for m in moves:
            state = state.apply_move(m)
        assert state.score == 150

    def test_4(self):
        state = read_state_from(
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

        moves = solve(state)
        for m in moves:
            state = state.apply_move(m)
        assert state.score == 309

    def test_ulearn(self):
        state = read_state_from(
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

        moves = solve(state)
        for m in moves:
            state = state.apply_move(m)
        assert state.score == 31571