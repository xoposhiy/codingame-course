import unittest
from heuristic import heuristic
from heuristic2 import heuristic2
from state import State, Move


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class HeuristicTests(unittest.TestCase):
    # def test_basic(self):
    #     chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
    #     s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
    def test_heruisic1(self):
        chs = [(7000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints):
                break
        self.assertEqual(s.checkpoint_index, len(s.checkpoints))

    def test_heruisic2(self):
        chs = [(7000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints) * 3:
                break
        self.assertEqual(s.checkpoint_index, len(s.checkpoints))


class HeuristicTests2(unittest.TestCase):
    # def test_basic(self):
    #     chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
    #     s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
    def test_heruisic1(self):
        chs = [(7000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints):
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints))

    def test_heruisic2(self):
        chs = [(7000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turnNumber = 0
        while turnNumber < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turnNumber += 1
            if s.checkpoint_index == len(s.checkpoints) * 3:
                break
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * 3)


if __name__ == '__main__':
    unittest.main()