import unittest
from conway import next_step

class FirstTest(unittest.TestCase):
    def test_empty(self):
        pairs = []
        assert next_step(pairs) == []







if __name__ == '__main__':
    unittest.main()