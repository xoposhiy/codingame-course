import math
from state import State


def estimate_state(state: State) -> float:
    """
    Задание 1.

    Возвращает оценку state.
    Чем больше число, тем более желаемый state.
    Чем больше checkpoint_index, тем лучше
    Чем ближе следующий чекпоинт, тем луче
    """
    xc, yc = state.next_checkpoint()
    dx = xc - state.x
    dy = yc - state.y
    dist_penalty = math.sqrt(dx * dx + dy * dy) / 100000.0
    return state.checkpoint_index - dist_penalty

