import unittest
import algorithms.list as list

class List(unittest.TestCase):

    def setUp(self):
        pass

    def test_list(self):
        bounds, m = [e for e in list.find_max_sub([-2, 3, -4, 5, 1, -5])]
        self.assertEqual(bounds, (3, 4))
        self.assertEqual(m, 6)


if __name__ == '__main__':
  unittest.main()

