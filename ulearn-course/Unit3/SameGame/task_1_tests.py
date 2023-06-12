import unittest
from samegame import *


class DfsTests(unittest.TestCase):
    def test_1(self):
        s = read_state_from([
            '1 1 2',
            '2 3 4'])
        area = s.dfs(0, 0, [])
        expected = [(0, 0)]
        assert area == expected

    def test_2(self):
        s = read_state_from([
            '1 1 2',
            '2 3 4'])
        area = s.dfs(0, 1, [])
        expected = [(0, 1), (1, 1)]
        assert area == expected

    def test_3(self):
        s = read_state_from([
            '2 2 1',
            '1 1 3',
            '1 2 3'])
        area = s.dfs(0, 0, [])
        expected = [(0, 0), (0, 1), (1, 1)]
        assert area == expected

    def test_4(self):
        s = read_state_from([
            '1 . 3 .',
            '2 1 1 1',
            '3 1 2 1'])
        area = s.dfs(1, 0, [])
        expected = [(1, 0), (1, 1), (2, 1), (3, 1), (3, 0)]
        assert area == expected

    def test_5(self):
        s = read_state_from([
            '1 1',
            '1 1'])
        area = s.dfs(0, 0, [])
        expected = [(0, 0), (0, 1), (1, 1), (1, 0)]
        assert area == expected
