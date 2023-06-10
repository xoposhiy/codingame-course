
def read_checkpoints():
    n = int(input())
    checkpoints = []
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        checkpoints.append((x, y))
    return checkpoints


def main():
    checkpoints = read_checkpoints()
    while True:
        checkpoint_index, x, y, vx, vy, angle = [int(i) for i in input().split()]
        checkpoint = checkpoints[checkpoint_index]
        # print(heuristic(checkpoint))


if __name__ == '__main__':
    main()
