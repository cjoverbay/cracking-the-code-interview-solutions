import unittest

from python.solution.chapter_01_arrays_and_strings import problem_1_1_is_unique

# Grab all specific implementations from this solution
to_test = []
for attr in [getattr(problem_1_1_is_unique, x) for x in dir(problem_1_1_is_unique)]:
    if callable(attr):
        to_test.append(attr)


class Tests(unittest.TestCase):

    def setUp(self):
        pass

    # Custom assert which logs function name on an error.
    # (To determine which implementation caused error)
    def assertEqualCall(self, func, params, expected):
        return self.assertEqual(func(*params), expected, 'in function ' + func.__name__)

    def test_empty(self):
        for implementation in to_test:
            self.assertEqualCall(implementation, [''], True)

    def test_all_different(self):
        for implementation in to_test:
            self.assertEqualCall(implementation, ['abcd'], True)

    def test_duplicates(self):
        for implementation in to_test:
            self.assertEqualCall(implementation, ['abad'], False)

