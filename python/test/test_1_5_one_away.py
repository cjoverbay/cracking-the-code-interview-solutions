import unittest

from python.solution.chapter_01_arrays_and_strings import problem_1_5_one_away

# Grab all specific implementations from this solution
implementations = []
for attr in [getattr(problem_1_5_one_away, x) for x in dir(problem_1_5_one_away)]:
    if callable(attr):
        implementations.append(attr)


class Tests(unittest.TestCase):

    # Custom assert which logs function name on an error.
    # (To determine which implementation caused error)
    def assertEqualCall(self, func, params, expected):
        return self.assertEqual(func(*params), expected, 'in function ' + func.__name__)

    def setUp(self):
        pass

    def test_empty(self):
        for check_one_away in implementations:
            self.assertEqual(check_one_away('', ''), True)

    def test_example_1(self):
        for check_one_away in implementations:
            self.assertEqual(check_one_away('pale', 'ple'), True)

    def test_example_2(self):
        for check_one_away in implementations:
            self.assertEqual(check_one_away('pales', 'pale'), True)

    def test_example_3(self):
        for check_one_away in implementations:
            self.assertEqual(check_one_away('pale', 'bale'), True)

    def test_example_4(self):
        for check_one_away in implementations:
            self.assertEqual(check_one_away('pale', 'bake'), False)

    def test_example_5(self):
        for check_one_away in implementations:
            self.assertEqual(check_one_away('pale', 'pae'), True)
