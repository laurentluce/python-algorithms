import unittest

import algorithms.generators as generators


class GeneratorsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_fib(self):
        fib = [e for e in generators.fib(10)]
        self.assertEqual(fib, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fib_empty(self):
        fib = [e for e in generators.fib(0)]
        self.assertEqual(fib, [])


if __name__ == '__main__':
    unittest.main()
