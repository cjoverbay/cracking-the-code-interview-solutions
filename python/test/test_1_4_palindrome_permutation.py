import unittest

from python.solution.chapter_01_arrays_and_strings import problem_1_4_palindrome_permutation

# Grab all specific implementations from this solution
implementations = []
for attr in [getattr(problem_1_4_palindrome_permutation, x) for x in dir(problem_1_4_palindrome_permutation)]:
    if callable(attr):
        implementations.append(attr)


class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_ignores_spaces(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome(''), True)

    def test_ignores_spaces(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome('a '), True)

    def test_ignores_caps(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome('aA'), True)

    def test_simple_1(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome('aab'), True)

    def test_simple_2(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome('abc'), False)

    def test_example_1(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome('Tact Coa'), True)

    def test_example_2(self):
        for is_perm_palindrome in implementations:
            self.assertEqual(is_perm_palindrome('amimMaDadam'), True)
