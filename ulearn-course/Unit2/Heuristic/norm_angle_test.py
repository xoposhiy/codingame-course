import unittest
from norm_angle import *


class NormAngleTests(unittest.TestCase):
    def test_norm_angle(self):
        assert norm_angle(360) == 0
        assert norm_angle(370) == 10
        assert norm_angle(350) == -10
        assert norm_angle(-10) == -10
        assert norm_angle(-360) == 0
        assert norm_angle(-370) == -10
        assert norm_angle(10) == 10


if __name__ == '__main__':
    unittest.main()