import unittest
from conway import (next_step, get_adjacent)

class FirstTest(unittest.TestCase):
    def test_empty(self):
        pairs = set()
        assert next_step(pairs) == set()

    def test_single(self):
        pairs = set([(0, 0)])
        assert next_step(pairs) == set()

    def test_get_adjacent(self):
        cell = (0, 0)
        expected = set([(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)])
        assert get_adjacent(cell) == expected
   



if __name__ == '__main__':
    unittest.main()
