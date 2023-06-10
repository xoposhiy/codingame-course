import math
from norm_angle import norm_angle


def is_time_to_brake(dx, dy, vx, vy):
    d = math.sqrt(dx * dx + dy * dy)
    v = math.sqrt(vx * vx + vy * vy)
    return v * 6 > d


def heuristic3(checkpoint, x, y, vx, vy, angle):
    """
    Если текущая скорость такая, что до следующего чекпоинта мы докатимся по инерции,
    то выключаем двигатель.
    """
    dx = checkpoint[0] - x
    dy = checkpoint[1] - y
    if is_time_to_brake(dx, dy, vx, vy):
        return f"{checkpoint[0]} {checkpoint[1]} 0 inertia"
    cp_angle = math.atan2(dy, dx) * 180 / math.pi
    da = norm_angle(cp_angle - angle)
    if abs(da) > 15:
        return f"{checkpoint[0]} {checkpoint[1]} 0 turn"
    return f"{checkpoint[0]} {checkpoint[1]} 200 thrust"

