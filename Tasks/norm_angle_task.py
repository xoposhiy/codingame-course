import math


def norm_angle(a: float) -> float:
    a = a % 360  # 0..360
    if a > 180:
        a -= 360  # -180..180
    return a
