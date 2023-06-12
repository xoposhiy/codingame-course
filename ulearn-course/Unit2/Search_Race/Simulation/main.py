
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

        best_moves = random_search(state)
        best_move = best_moves[0]
        print(best_move)
        state.simulate(best_move)
        predicted_state = state


if __name__ == '__main__':
    main()
