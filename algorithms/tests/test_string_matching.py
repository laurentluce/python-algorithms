import unittest
import string_matching

class StringMatchingTest(unittest.TestCase):
    
  def test_string_matching_naive(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEquals(string_matching.string_matching_naive(t, s), [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEquals(string_matching.string_matching_naive(t, s), [])

  def test_string_matching_rabin_karp(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEquals(string_matching.string_matching_rabin_karp(t, s), [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEquals(string_matching.string_matching_rabin_karp(t, s), [])

  def test_string_matching_knuth_morris_pratt(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEquals(string_matching.string_matching_knuth_morris_pratt(t, s), [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEquals(string_matching.string_matching_knuth_morris_pratt(t, s), [])

  def test_string_matching_boyer_moore_horspool(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEquals(string_matching.string_matching_boyer_moore_horspool(t, s), [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEquals(string_matching.string_matching_boyer_moore_horspool(t, s), [])

if __name__ == '__main__':
    unittest.main()

