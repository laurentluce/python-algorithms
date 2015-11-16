import unittest
import algorithms.list as list

class List(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_max_sub(self):
        bounds, m = [e for e in list.find_max_sub([-2, 3, -4, 5, 1, -5])]
        self.assertEqual(bounds, (3, 4))
        self.assertEqual(m, 6)

    def test_find_int_first_half(self):
        idx = list.find_int(4, [1, 2, 4, 5, 7, 9])
        self.assertEqual(idx, 2)

    def test_find_int_second_half(self):
        idx = list.find_int(7, [1, 2, 4, 5, 7, 9])
        self.assertEqual(idx, 4)

    def test_find_int_not_found(self):
        idx = list.find_int(3, [1, 2, 4, 5, 7, 9])
        self.assertIsNone(idx)

    def test_find_int_single_element_list(self):
        idx = list.find_int(3, [3,])
        self.assertEqual(idx, 0)

    def test_find_int_empty_list(self):
        idx = list.find_int(3, [])
        self.assertIsNone(idx)

if __name__ == '__main__':
  unittest.main()

