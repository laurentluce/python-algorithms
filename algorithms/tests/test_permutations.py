import unittest

import algorithms.permutations as permutations


class GeneratorsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_permutations(self):
        p = [e for e in permutations.permutations([1, 2, 3])]
        self.assertEqual(p, [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2],
                             [3, 1, 2], [3, 2, 1]])

    def test_permutations_single(self):
        p = [e for e in permutations.permutations([1])]
        self.assertEqual(p, [[1]])


if __name__ == '__main__':
    unittest.main()
