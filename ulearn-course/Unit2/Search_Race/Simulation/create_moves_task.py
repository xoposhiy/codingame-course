import random
from state import Move


def create_random_moves(depth: int):
    """
    Задание 2.

    Создает и возвращает массив из depth случайных объектов Move.
    """
    moves = []
    for i in range(depth):
        thrust = min(200, max(0, random.randint(-50, 250)))
        moves.append(Move(random.randint(0, 16000), random.randint(0, 9000), thrust, "rnd"))
        # moves.append(create_random_move())
    return moves


# def create_random_move() -> Move:
#     thrust = min(200, max(0, random.randint(-50, 250)))
#     return Move(random.randint(0, 16000), random.randint(0, 9000), thrust, "rnd")
