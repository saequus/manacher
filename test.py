import unittest
import time

import manacher_util


class TestGetPalindromeLength(unittest.TestCase):

    def test_no_palindrome(self):
        string = 'abc'
        self.assertEqual(manacher_util.get_palindrome_length(string, 1), 0)

    def test_left_border(self):
        string = 'abc'
        self.assertEqual(manacher_util.get_palindrome_length(string, 0), 0)

    def test_right_border(self):
        string = 'abc'
        self.assertEqual(manacher_util.get_palindrome_length(string, 2), 0)

    def test_palindrome(self):
        string = 'abbbc'
        self.assertEqual(manacher_util.get_palindrome_length(string, 2), 1)


class TestManacher(unittest.TestCase):

    def test_same_char(self):
        input_data = 'a' * 5
        expected = [0, 0, 1, 1, 2, 2, 2, 1, 1, 0, 0]
        self.assertEqual(manacher_util.manacher(input_data), expected)

    def test_no_overlap(self):
        input_data = 'aapmm'
        expected = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual(manacher_util.manacher(input_data), expected)

    def test_no_palindromes(self):
        input_data = 'abcdefghijklmonp'
        expected = [0 for _ in range(len(input_data) * 2 + 1)]
        self.assertEqual(manacher_util.manacher(input_data), expected)

    def test_time_complexity(self):

        def timed_run(string):
            start = time.time()
            manacher_util.manacher(string)
            return time.time() - start

        results = [timed_run('a'* _) for _ in range(100, 1000, 100)]
        for small, big in zip(results[1:], results[:-1]):
            self.assertGreater(small*10, big)


class TestGetPalindromeNumber(unittest.TestCase):

    def test_no_palindromes(self):
        input_data = 'abcdefghijklmnoprst'
        expected = 0
        self.assertEqual(
            manacher_util.get_palindrome_number(input_data), expected)

    def test_palindromes(self):
        input_data = 'q'*5
        expected = 10
        print(manacher_util.manacher(input_data))
        self.assertEqual(
            manacher_util.get_palindrome_number(input_data), expected)


class TestGetLongestPalindromeSubstring(unittest.TestCase):

    def test_short_length(self):
        input_data = 'babcbacc'
        expected = 'abcba'
        self.assertEqual(
            manacher_util.get_longest_palindrome(input_data), expected)

    def test_middle_length(self):
        input_data = '23dx44ecefece44feszvsdf'
        expected = '44ecefece44'
        self.assertEqual(
            manacher_util.get_longest_palindrome(input_data), expected)

    def test_long_length(self):
        input_data = 'we02afhthfa20ddsmmeekdmeemdkeemm239dx..xd9322'
        expected = 'mmeekdmeemdkeemm'
        self.assertEqual(
            manacher_util.get_longest_palindrome(input_data), expected)
