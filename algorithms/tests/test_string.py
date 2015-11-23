import unittest

import algorithms.string as string


class StringTest(unittest.TestCase):

    def test_atoi(self):
        self.assertEqual(string.atoi('123'), 123)

    def test_atoi_neg(self):
        self.assertEqual(string.atoi('-123'), -123)

    def test_atoi_empty_string(self):
        self.assertRaises(ValueError, string.atoi, '')

    def test_reverse_string_words(self):
        s = 'word1 word2 word3'
        s = string.reverse_string_words(s)
        self.assertEqual(s, 'word3 word2 word1')

    def test_reverse_string_word(self):
        s = 'word1'
        s = string.reverse_string_words(s)
        self.assertEqual(s, 'word1')

    def test_string_matching_naive(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEqual(string.string_matching_naive(t, s), [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEqual(string.string_matching_naive(t, s), [])

    def test_string_matching_rabin_karp(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEqual(string.string_matching_rabin_karp(t, s), [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEqual(string.string_matching_rabin_karp(t, s), [])

    def test_string_matching_knuth_morris_pratt(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEqual(string.string_matching_knuth_morris_pratt(t, s),
                         [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEqual(string.string_matching_knuth_morris_pratt(t, s), [])

    def test_string_matching_boyer_moore_horspool(self):
        t = 'ababbababa'
        s = 'aba'
        self.assertEqual(string.string_matching_boyer_moore_horspool(t, s),
                         [0, 5, 7])
        t = 'ababbababa'
        s = 'abbb'
        self.assertEqual(string.string_matching_boyer_moore_horspool(t, s), [])

        s = 'ababbababa'
        t = 'abbb'
        self.assertEqual(string.string_matching_boyer_moore_horspool(t, s), [])


if __name__ == '__main__':
    unittest.main()
