import math
from state import Move


def heuristic(checkpoint):
    """На полном ходу летим к следующему флагу"""
    return f"{checkpoint[0]} {checkpoint[1]} 200"

