import unittest
from samegame import *


class MovesTests(unittest.TestCase):
    def test_apply_move(self):
        s = read_state_from([
            '1 1 2',
            '2 3 4'])
        move = [m for m in s.moves() if (0, 1) in m][0]
        s = s.apply_move(move)
        expected = [
            '. . 2',
            '2 3 4']
        assert str(s).split('\n') == expected

    def test_apply_move_fly_down(self):
        s = read_state_from([
            '2 2 1',
            '1 1 3',
            '1 2 3'])
        move = [m for m in s.moves() if (0, 1) in m][0]
        s = s.apply_move(move)
        expected = [
            '. . 1',
            '. 2 3',
            '2 2 3']
        assert str(s).split('\n') == expected

    def test_apply_move_compaction(self):
        s = read_state_from([
            '1 . 3 .',
            '2 1 1 1',
            '3 1 2 1'])
        move = [m for m in s.moves() if (1, 0) in m][0]
        s = s.apply_move(move)
        expected = [
            '1 .',
            '2 3',
            '3 2']
        assert str(s).split('\n') == expected


    def test_moves_empty_column(self):
        s = read_state_from([
            '1 1',
            '1 1'])
        move = [m for m in s.moves() if (1, 0) in m][0]
        s = s.apply_move(move)
        expected = ['.']
        assert str(s).split('\n') == expected


    def test_moves_large_area(self):
        s = read_state_from([
            '2 1 1 4 1',
            '1 2 1 4 1',
            '1 1 1 4 4',
            '1 2 1 4 4',
            '1 1 2 4 3'])
        move = [m for m in s.moves() if (1, 0) in m][0]
        s = s.apply_move(move)
        expected = [
            '. . . 4 1',
            '. . . 4 1',
            '. . . 4 4',
            '. 2 . 4 4',
            '2 2 2 4 3']
        assert str(s).split('\n') == expected

        move = [m for m in s.moves() if (1, 0) in m][0]
        s = s.apply_move(move)
        expected = [
            '4 1',
            '4 1',
            '4 4',
            '4 4',
            '4 3']
        assert str(s).split('\n') == expected


def test_solve():
    """
    Запускаем функцию solve на отдельном тесте.
    Печатаем на консоль количество очков, которое набирает наш алгоритм на этом тесте
    """
    state = read_state_from(
        '3 1 1 4 1 0 4 0 4 4 1 1 0 2 3\n3 3 2 0 4 4 1 3 1 2 0 0 4 0 4\n0 2 3 4 3 0 3 0 0 3 4 4 1 1 1\n2 3 4 0 2 3 0 2 4 4 4 3 0 2 3\n1 2 1 3 1 2 0 1 2 1 0 3 4 0 1\n0 4 4 3 0 3 4 2 2 2 0 2 3 4 0\n2 4 3 4 2 3 1 1 1 3 4 1 0 3 1\n1 0 0 4 0 3 1 2 1 0 4 1 3 3 1\n1 3 3 2 0 4 3 1 3 0 4 1 0 0 3\n0 3 3 4 2 3 0 0 2 1 2 3 4 0 1\n0 4 1 2 0 1 3 4 3 3 4 1 4 0 4\n2 2 3 1 0 4 0 1 2 4 1 3 3 0 1\n3 3 0 2 3 2 1 4 3 1 3 0 2 1 3\n1 0 3 2 1 4 4 4 4 0 4 2 1 3 4\n1 0 1 0 1 1 2 2 1 0 0 1 4 3 2'
        .splitlines())
    moves = chokudai_solve(state)
    print(moves)
    for m in moves:
        state = state.apply_move(m)
    print(state.score)
