import sys
import pytest
from norm_angle_task import *


def test_norm_angle():
    assert norm_angle(360) == 0
    assert norm_angle(370) == 10
    assert norm_angle(350) == -10
    assert norm_angle(-10) == -10
    assert norm_angle(-360) == 0
    assert norm_angle(-370) == -10
    assert norm_angle(10) == 10