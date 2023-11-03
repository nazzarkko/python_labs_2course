import unittest

from main import min_knight_moves


class TestKnightMoves(unittest.TestCase):
    def test_min_knight_moves(self):
        self.assertEqual(min_knight_moves(8, (7, 0), (0, 7)), 6)
        self.assertEqual(min_knight_moves(8, (0, 0), (7, 7)), 6)
        self.assertEqual(min_knight_moves(8, (2, 3), (6, 4)), 3)

if __name__ == '__main__':
    unittest.main()