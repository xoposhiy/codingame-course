import unittest
from state import State
from estimate_task import estimate_state


class EstimateTests(unittest.TestCase):
    def test_zero_delta(self):
        chs = [(2000, 2000), (12000, 7000)]
        s1 = State(chs, 0, 2000, 2000, 0, 0, 0)
        s2 = State(chs, 0, 2000, 2000, 0, 0, 0)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 == score2

    def test_zero_delta_2(self):
        chs = [(2000, 2000), (12000, 7000)]
        s1 = State(chs, 0, 1000, 2000, 0, 0, 0)
        s2 = State(chs, 0, 2000, 1000, 0, 0, 0)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 == score2

    def test_zero_delta_3(self):
        chs = [(2000, 2000), (12000, 7000)]
        s1 = State(chs, 0, 1050, 1000, 0, 0, 0)
        s2 = State(chs, 0, 3000, 2950, 0, 0, 1)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 == score2

    def test_one_better_than_other(self):
        chs = [(5000, 7000), (12000, 7000)]
        s1 = State(chs, 0, 1000, 1000, 0, 0, 45)
        s2 = State(chs, 0, 3000, 3000, 0, 0, 45)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 < score2

    def test_one_better_than_other_2(self):
        chs = [(5000, 7000), (12000, 7000)]
        s1 = State(chs, 0, 3000, 3000, 0, 0, 45)
        s2 = State(chs, 0, 6000, 9000, 0, 0, 45)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 < score2

    def test_one_better_than_other_3(self):
        chs = [(5000, 7000), (12000, 7000)]
        s1 = State(chs, 1, 3000, 3000, 0, 0, 45)
        s2 = State(chs, 0, 6000, 9000, 0, 0, 45)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 > score2

    def test_one_better_than_other_4(self):
        chs = [(0, 0), (16000, 9000)]
        s1 = State(chs, 1, 0, 0, 0, 0, 45)
        s2 = State(chs, 0, 0, 0, 0, 0, 45)
        score1 = estimate_state(s1)
        score2 = estimate_state(s2)
        assert score1 > score2


