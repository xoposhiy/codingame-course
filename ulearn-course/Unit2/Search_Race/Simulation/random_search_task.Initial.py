import sys
import math
import time
from estimate_task import estimate_state
from create_moves_task import create_random_moves
from state import State, Move


def random_search(state: State, depth: int = 4) -> list[Move]:
    """
    Задание 3.

    Реализация алгоритма Monte-Carlo (другое название — случайный поиск)

    Пока есть время — создаёт новую последовательность из depth случайных ходов с помощью функции create_random_moves
    Симулирует эту последовательность ходов.
    Оценивает финальное состояние после эти depth шагов с помощью функции estimate и запоминает лучшую.

    Когда время закончилось, возвращает лучшую последовательность ходов.

    На каждый ход даётся 50 миллисекунд.
    Чтобы засечь время, воспользуйтесь функцией time.time() — она возвращает текущее время в секундах (дробное число).

    Когда закончите, подберите подходящее значение глубины (depth) экспериментально.
    """
    best_moves = []
    best_score = -math.inf
    simulations_count = 0  # количество случайных решений, которые успели рассмотреть

    # ... тут должен быть ваш код ...

    pass