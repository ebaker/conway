import unittest
from conway import (next_step, get_adjacent, lives_on)

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

class LivesOnTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_one_neighbor(self):
        live_cells_list = [(0,x) for x in range(1)]
        cell = live_cells_list[0]
        live_cells = set(live_cells_list)
        state = lives_on(cell, live_cells)
        assert state == False
    

   



if __name__ == '__main__':
    unittest.main()
