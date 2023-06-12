import unittest
from create_moves_task import create_random_moves


class CreateMovesTests(unittest.TestCase):
    def test_one_move(self):
        depth = 1
        moves = create_random_moves(depth)
        assert len(moves) == depth

    def test_more_moves(self):
        depth = 5
        moves = create_random_moves(depth)
        moves_set = set(moves)
        assert len(moves_set) == depth

    def test_lots_of_moves(self):
        # считать матожидание
        depth = 100000
        moves = create_random_moves(depth)
        moves_set = set(moves)
        assert len(moves_set) == depth
