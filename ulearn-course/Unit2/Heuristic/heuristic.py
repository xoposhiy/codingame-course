import math
from state import Move


def heuristic(checkpoints):
    """На полном ходу летим к следующему флагу"""
    return Move(checkpoints[0], checkpoints[1], 200)

