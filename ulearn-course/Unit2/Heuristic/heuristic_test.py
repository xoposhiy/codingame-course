import unittest
from heuristic import heuristic
from heuristic2 import heuristic2
from state import State, Move


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class HeuristicTests(unittest.TestCase):
    def test_1(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints):
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints))

    # def test_2(self):
    #     chs = [(7000, 7000)]
    #     s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
    #     turnNumber = 0
    #     while turnNumber < 600:
    #         s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
    #         turnNumber += 1
    #         if s.checkpoint_index == len(s.checkpoints) * 3:
    #             break
    #     self.assertEqual(s.checkpoint_index, len(s.checkpoints))
    #
    # def test_3(self):
    #     chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
    #     s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
    #     turnNumber = 0
    #     while turnNumber < 600:
    #         s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
    #         turnNumber += 1
    #         if s.checkpoint_index == len(s.checkpoints) * 3:
    #             break
    #     self.assertEqual(s.checkpoint_index, 2)


class HeuristicTests2(unittest.TestCase):
    def test_1(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints):
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints))

    def test_2(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints) * 3:
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * 3)

    def test_3(self):
        chs = [(8500, 1000), (10975,2025), (12000, 4500), (8500, 8000), (3500, 5500), (3500, 2500), (4000, 1000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints) * 3:
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * 3)

    def test_4(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints) * 3:
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * 3)


if __name__ == '__main__':
    unittest.main()