import math
from norm_angle import norm_angle


def heuristic2(checkpoint: (int, int), x: int, y: int, angle: int) -> str:
    """
    Включаем полный ход, если смотрим почти на следующий флаг.
    Поворачиваемся в сторону следующего флага.
    """
    cx, cy = checkpoint
    dx = cx - x
    dy = cy - y
    cp_angle = math.atan2(dy, dx) * 180 / math.pi
    da = norm_angle(cp_angle - angle)
    if abs(da) > 15:
        return f"{cx} {cy} 0 turn"
    return f"{cx} {cy} 200 thrust"

