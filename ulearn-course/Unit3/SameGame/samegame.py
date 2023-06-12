import heapq
import sys
import time
from typing import Optional


# В этом файле активно используются type hints — возможность указать типы
# аргументов и возвращаемого результата у функций вот, например, так:
#
# def f(x: int, y: str) -> float:
#
# Первый аргумент функции f — это целое число, второй — строка, а возвращает функция число с плавающей точкой
# С ними должно быть понятнее, что именно нужно передавать функции и что она возвращает.
#
# Какие ещё типы можно указывать кроме int и str? Много разных. Вот несколько примеров:
#   list[int] — список целых чисел
#   list[list[int]] — список списков целых чисел
#   Optional[str] — либо строка, либо None


class State:
    def __init__(self, columns: 'list[list[int]]', score: int = 0, turn_number: int = 0, previous_state = None):
        self.columns = columns
        self.score = score
        self.turn_number = turn_number
        self.previous_state = previous_state

    def __str__(self):
        w = len(self.columns)
        if w == 0:
            return '.'
        h = max(len(col) for col in self.columns)
        rows = []
        for y in range(h - 1, -1, -1):
            row = []
            for x in range(w):
                row.append('.' if y >= len(self.columns[x]) else str(self.columns[x][y]))
            rows.append(' '.join(row))
        return '\n'.join(rows)

    def dfs(self, x: int, y: int, move: 'list[tuple[int, int]]'):
        """
        Задание 1
        Поиск в глубину.
            На вход: стартовый тайл (x, y), список тайлов, уже вошедших в одноцветную область move
            Результат: в move добавлены все тайлы, образующие связную одноцветную область с тайлом (x, y)

        Реализация:
            1. Включите тайл (x, y) в move.
            2. Для каждого соседнего тайла того же цвета, которого ещё нет в move:
                запустите из него рекурсивно dfs
            3. Верните move
        """
        w = len(self.columns)
        move.append((x, y))
        color = self.columns[x][y]
        for ny, nx in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
            if 0 <= nx < w and 0 <= ny < len(self.columns[nx]):
                nxt = (nx, ny)
                if self.columns[nx][ny] == color and nxt not in move:
                    self.dfs(nx, ny, move)
        return move

    def moves(self) -> 'list[list[tuple[int, int]]]':
        """
        Задание 2
        Возвращает список ходов, которые можно отправить в apply_move.

        Реализация:
        1. Создайте множество уже посещённых тайлов visited = set()
        2. Создайте список ходов, в котором будет накапливаться результат.
        3. Из каждого ещё не посещённого тайла:
            1) Запустите обход одноцветной области (метод dfs ниже).
            2) Найденную область добавьте в список ходов
            3) Все клетки найденной области добавьте в посещённые.
        4. Верните список ходов
        """
        res = []
        used = set()
        for x, col in enumerate(self.columns):
            for y, color in enumerate(col):
                if (x, y) not in used:
                    area = self.dfs(x, y, [])
                    if len(area) > 1:
                        res.append(area)
                    for m in area:
                        used.add(m)
        return res

    def apply_move(self, move: 'list[tuple[int, int]]') -> 'State':
        """
        Задание 3
        Применяет ход и возвращает новое состояние (не меняя текущее!)

        Реализация:
            1. Создайте новый пустой список новых столбцов
            2. Для каждого столбца:
                1. Создайте пустой новый столбец
                2. Добавьте в него все тайлы исходного столбца, которого нет в списке тайлов применяемого хода.
                3. Добавьте в список столбцов новый столбец, если он получился не пустым
            3. Создайте из списка новых столбцов новый State и верните его
        """
        n = len(move)
        score = self.score + (n - 2) * (n - 2)
        columns = []
        for x, col in enumerate(self.columns):
            new_col = []
            for y, v in enumerate(col):
                if (x, y) not in move:
                    new_col.append(v)
            if len(new_col) > 0:
                columns.append(new_col)
        if len(columns) == 0:
            score += 1000
        return State(columns, score, self.turn_number + 1, self)

def estimate(state: State) -> float:
    """
    Задание 4
    Чем больше возвращаемое число, тем лучше это состояние.
    """
    return state.score + sum([(len(m)-2)**2 for m in state.moves()])

def greedy_ai(state: State, estimate_state) -> 'Optional[list[tuple[int, int]]]':
    """
    Задание 5
    Среди всех доступных ходов выбирает тот, после применения которого, estimate_state дает максимальное значение.
    Возвращает ход или None, если ходов нет.
    """
    scored_moves = [(estimate_state(state.apply_move(m)), i, m) for i, m in enumerate(state.moves())]
    if len(scored_moves) == 0:
        return None
    best_move = max(scored_moves)
    return best_move[2]



def solve(state: State) -> 'list[list[tuple[int, int]]]':
    """
    На codingame.com на первый ход дают 20 секунд, а на последующие всего по 50ms.
    Поэтому выгодно решить полностью весь уровень на первом ходу и вернуть список всех ходов.
    """
    solution = []
    while True:
        move = greedy_ai(state, estimate)
        if move is None:
            break
        solution.append(move)
        state = state.apply_move(move)
    return solution


def read_state_from(lines: 'list[str]') -> State:
    """
    Читает состояние из списка строк.
    Удобно использовать при тестировании
    """
    rows = []
    for line in lines:
        row = []
        for color in line.split():
            row.append(-1 if color == '.' else int(color))
        rows.append(row)

    # Переводим в наш формат: список столбцов, клетки в которых перечислены снизу вверх, без пустых клеток
    cols = [[row[x] for row in reversed(rows) if row[x] != -1] for x in range(len(rows[0]))]
    return State(cols)


def read_state() -> State:
    """
    Читает состояние из консоли
    """
    lines = [input() for _ in range(15)]
    return read_state_from(lines)


def main():
    state = read_state()
    print(state, file=sys.stderr)
    moves = solve(state)
    # moves = chokudai_solve(state)
    for move in moves:
        x, y = move[0]
        print(x, y)
        read_state()


if __name__ == '__main__':
    main()
