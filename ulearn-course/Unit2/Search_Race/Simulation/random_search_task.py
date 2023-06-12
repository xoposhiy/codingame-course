import sys
import math
import time
from estimate_task import estimate_state
from create_moves_task import create_random_moves
from state import State, Move


def random_search(state: State, depth: int = 4):
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

    start_time = time.time()
    while time.time() - start_time < 0.045:
    # for i in range(1000):
        moves = create_random_moves(depth)
        end_state = state.copy()
        for move in moves:
            end_state.simulate(move)
        score = estimate_state(end_state)
        simulations_count += 1
        if score > best_score:
            best_score = score
            best_moves = moves
    # отладочный вывод: лучший, найденный счёт; количество изученных случайных решений; лучшая последовательность ходов
    # print(best_score, simulations_count, list(map(str, best_moves)), file=sys.stderr)
    return best_moves
