import random
import sys
import math
import time


def norm_angle(a):
    a = a % 360  # 0..360
    if a > 180:
        a -= 360  # -180..180
    return a


class Move:
    def __init__(self, x, y, thrust, message=""):
        self.x, self.y, self.thrust, self.message = x, y, thrust, message

    def __str__(self):
        return f'{self.x} {self.y} {self.thrust} {self.message}'


class State:
    def __init__(self, checkpoints, checkpoint_index, x, y, vx, vy, angle):
        self.checkpoints = checkpoints
        self.checkpoint_index = checkpoint_index
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = angle

    def __str__(self):
        return f'State(checkpoints, {self.checkpoint_index}, {self.x}, {self.y}, {self.vx}, {self.vy}, {self.angle})'

    def copy(self):
        return State(self.checkpoints, self.checkpoint_index, self.x, self.y, self.vx, self.vy, self.angle)

    def next_checkpoint(self):
        return self.checkpoints[self.checkpoint_index % len(self.checkpoints)]

    def simulate(self, move: Move):
        desired_angle = 180 * math.atan2(move.y - self.y, move.x - self.x) / math.pi
        da = norm_angle(desired_angle - self.angle)
        da = max(-18, min(18, da))
        self.angle = self.angle + da
        self.vx += move.thrust * math.cos(self.angle * math.pi / 180)
        self.vy += move.thrust * math.sin(self.angle * math.pi / 180)
        self.x = int(self.x + self.vx)
        self.y = int(self.y + self.vy)
        self.vx = int(0.85 * self.vx)
        self.vy = int(0.85 * self.vy)
        self.angle = round(self.angle) % 360
        xc, yc = self.next_checkpoint()
        dx, dy = self.x - xc, self.y - yc
        if dx * dx + dy * dy <= 600 * 600:
            self.checkpoint_index += 1


def estimate(state):
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


def create_random_moves(depth):
    """
    Задание 2.

    Создает и возвращает массив из depth случайных объектов Move.
    """
    moves = []
    for i in range(depth):
        moves.append(create_random_move())
    return moves


def create_random_move():
    thrust = min(200, max(0, random.randint(-50, 250)))
    return Move(random.randint(0, 16000), random.randint(0, 9000), thrust, "rnd")


def random_search(state, depth=4):
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
        score = estimate(end_state)
        simulations_count += 1
        if score > best_score:
            best_score = score
            best_moves = moves
    # отладочный вывод: лучший, найденный счёт; количество изученных случайных решений; лучшая последовательность ходов
    # print(best_score, simulations_count, list(map(str, best_moves)), file=sys.stderr)
    return best_moves


def get_best_move(state):
    best_moves = random_search(state)
    best_move = best_moves[0]
    return best_move


def read_checkpoints():
    n = int(input())  # количество чекпоинтов
    checkpoints = []
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        checkpoints.append((x, y))
    return checkpoints


def main():
    checkpoints = read_checkpoints()
    print(f'checkpoints={checkpoints}', file=sys.stderr)
    predicted_state = None
    best_moves = None
    while True:
        state = State(checkpoints, *list(map(int, input().split())))
        print(state, file=sys.stderr)
        if predicted_state:
            print(predicted_state, file=sys.stderr)
            # Проверка, что наша симуляция работает точно так же как и официальная.
            # Если раскомментировать строку ниже, то решение начнет падать с ошибкой каждый раз,
            # когда наша симуляция ошиблась, предсказывая к чему приведет наш предыдущий ход
            # assert str(predicted_state) == str(state)

        # best_moves = random_search(state)
        # best_move = best_moves[0]
        best_move = get_best_move(state)
        print(best_move)
        state.simulate(best_move)
        predicted_state = state


if __name__ == '__main__':
    main()
