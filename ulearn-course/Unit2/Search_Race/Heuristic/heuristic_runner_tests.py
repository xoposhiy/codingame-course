import unittest
from heuristic import heuristic
from heuristic2 import heuristic2
from heuristic3 import heuristic3
from heuristic4 import heuristic4
from visualizer_state import State, Move


def parse_move(line: str):
    f = line.split(" ")
    return Move(int(f[0]), int(f[1]), int(f[2]))


class HeuristicTests(unittest.TestCase):
    def test_two_points(self):
        chs = [(2000, 2000), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 2
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_zig_zag(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turn_number = 0
        laps_number = 1
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_half_round_and_round(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 86, [], [])
        turn_number = 0
        laps_number = 1
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic(s.next_checkpoint())))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)


class Heuristic2Tests(unittest.TestCase):
    def test_two_points(self):
        chs = [(2000, 2000), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_zig_zag(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turn_number = 0
        laps_number = 3
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_three_random(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        turn_number = 0
        laps_number = 3
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_tokio_drift(self):
        chs = [(1000, 1000), (12000, 1000), (12500, 2500), (13000, 4000),
               (12500, 5500), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_round_and_round(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000),
               (8000, 7000), (7500, 5500), (7500, 2500), (8000, 1000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 72, [], [])
        turn_number = 0
        laps_number = 3
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_hold_the_line(self):
        chs = [(1000, 4500), (2500, 3905), (4000, 5095), (5500, 3905),
               (7000, 5095), (8500, 3905), (10000, 5095), (11500, 3905)]
        s = State(chs, 0, 1000, 4500, 0, 0, 338, [], [])
        turn_number = 0
        laps_number = 3
        while turn_number < 600:
            s.simulate_move(parse_move(heuristic2(s.next_checkpoint(), s.x, s.y, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)


class Heuristic3Tests(unittest.TestCase):
    def test_two_points(self):
        chs = [(2000, 2000), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic3(s.next_checkpoint(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_zig_zag(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic3(s.next_checkpoint(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_three_random(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic3(s.next_checkpoint(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_tokio_drift(self):
        chs = [(1000, 1000), (12000, 1000), (12500, 2500), (13000, 4000),
               (12500, 5500), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic3(s.next_checkpoint(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_round_and_round(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000),
               (8000, 7000), (7500, 5500), (7500, 2500), (8000, 1000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 72, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic3(s.next_checkpoint(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_hold_the_line(self):
        chs = [(1000, 4500), (2500, 3905), (4000, 5095), (5500, 3905),
               (7000, 5095), (8500, 3905), (10000, 5095), (11500, 3905)]
        s = State(chs, 0, 1000, 4500, 0, 0, 338, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic3(s.next_checkpoint(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)


class Heuristic4Tests(unittest.TestCase):
    def test_two_points(self):
        chs = [(2000, 2000), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic4(s.next_checkpoint(),
                                                  s.next_checkpoint2(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_zig_zag(self):
        chs = [(1000, 1000), (15000, 8000), (1000, 8000), (15000, 5000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 0, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic4(s.next_checkpoint(),
                                                  s.next_checkpoint2(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_three_random(self):
        chs = [(10353, 1986), (2757, 4659), (3358, 2838)]
        s = State(chs, 0, 10353, 1986, 100, 200, 161, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic4(s.next_checkpoint(),
                                                  s.next_checkpoint2(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_tokio_drift(self):
        chs = [(1000, 1000), (12000, 1000), (12500, 2500), (13000, 4000),
               (12500, 5500), (12000, 7000)]
        s = State(chs, 0, 1000, 1000, 0, 0, 45, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic4(s.next_checkpoint(),
                                                  s.next_checkpoint2(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_round_and_round(self):
        chs = [(12000, 1000), (12500, 2500), (12500, 5500), (12000, 7000),
               (8000, 7000), (7500, 5500), (7500, 2500), (8000, 1000)]
        s = State(chs, 0, 12000, 1000, 0, 0, 72, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic4(s.next_checkpoint(),
                                                  s.next_checkpoint2(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)

    def test_hold_the_line(self):
        chs = [(1000, 4500), (2500, 3905), (4000, 5095), (5500, 3905),
               (7000, 5095), (8500, 3905), (10000, 5095), (11500, 3905)]
        s = State(chs, 0, 1000, 4500, 0, 0, 338, [], [])
        turn_number = 0
        laps_number = 3

        while turn_number < 600:
            s.simulate_move(parse_move(heuristic4(s.next_checkpoint(),
                                                  s.next_checkpoint2(),
                                                  s.x, s.y, s.vx, s.vy, s.angle)))
            turn_number += 1
        self.assertGreaterEqual(s.checkpoint_index, len(s.checkpoints) * laps_number)
