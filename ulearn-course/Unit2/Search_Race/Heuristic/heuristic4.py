import math
from norm_angle import norm_angle


def is_time_to_brake(dx, dy, vx, vy):
    d = math.sqrt(dx * dx + dy * dy)
    v = math.sqrt(vx * vx + vy * vy)
    return v * 6 > d


def heuristic4(checkpoint, next_checkpoint, x, y, vx, vy, angle):
    """
    Если текущая скорость такая, что до следующего чекпоинта мы докатимся по инерции,
    то выключаем двигатель и поворачиваемся к следующему чекпоинту.
    """
    dx = checkpoint[0] - x
    dy = checkpoint[1] - y
    if is_time_to_brake(dx, dy, vx, vy):
        return f"{next_checkpoint[0]} {next_checkpoint[1]} 0 turn_to_next"
    cp_angle = math.atan2(dy, dx) * 180 / math.pi
    da = norm_angle(cp_angle - angle)
    if abs(da) > 5:
        return f"{checkpoint[0]} {checkpoint[1]} 0 turn_to_cur"
    return f"{checkpoint[0]} {checkpoint[1]} 200 thrust"


