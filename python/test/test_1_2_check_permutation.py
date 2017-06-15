import unittest

from python.solution.chapter_01_arrays_and_strings import problem_1_2_check_permutation

# Grab all specific implementations from this solution
implementations = []
for attr in [getattr(problem_1_2_check_permutation, x) for x in dir(problem_1_2_check_permutation)]:
    if callable(attr):
        implementations.append(attr)


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    # Unit Tests Here
    def test_simple_permutation(self):
        for is_permutation in implementations:
            self.assertEqual(is_permutation('god', 'dog'), True)

    def test_single_letter(self):
        for is_permutation in implementations:
            self.assertEqual(is_permutation('a', 'a'), True)

    def test_same_word(self):
        for is_permutation in implementations:
            self.assertEqual(is_permutation('god', 'god'), True)

    def test_different_lengths(self):
        for is_permutation in implementations:
            self.assertEqual(is_permutation('go', 'god'), False)

    def test_almost_permutation(self):
        for is_permutation in implementations:
            self.assertEqual(is_permutation('food', 'doom'), False)
