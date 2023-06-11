import unittest
from norm_angle import *


class NormAngleTests(unittest.TestCase):
    def test_norm_angle(self):
        assert norm_angle(360) == 0
        assert norm_angle(-360) == 0
        assert norm_angle(350) == -10
        assert norm_angle(-350) == 10
        assert norm_angle(370) == 10
        assert norm_angle(-370) == -10
        assert norm_angle(10) == 10
        assert norm_angle(-10) == -10
        assert norm_angle(180) == 180
        assert norm_angle(-180) == 180
        assert norm_angle(181) == -179
        assert norm_angle(-181) == 179
        assert norm_angle(270) == -90
        assert norm_angle(-270) == 90
        assert norm_angle(630) == -90
        assert norm_angle(-630) == 90
        assert norm_angle(400) == 40
        assert norm_angle(-846) == -126
        assert norm_angle(254) == -106
        assert norm_angle(523) == 163



if __name__ == '__main__':
    unittest.main()