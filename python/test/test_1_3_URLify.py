import unittest

from python.solution.chapter_01_arrays_and_strings import problem_1_3_URLify

# Grab all specific implementations from this solution
implementations = []
for attr in [getattr(problem_1_3_URLify, x) for x in dir(problem_1_3_URLify)]:
    if callable(attr):
        implementations.append(attr)


class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_handles_spaces(self):
        for urlify in implementations:
            self.assertSequenceEqual(urlify([c for c in 'Mr John Smith    ']), [c for c in 'Mr%20John%20Smith'])

    def test_handles_empty(self):
        for urlify in implementations:
            self.assertSequenceEqual(urlify([]), [])

    def test_handles_no_spaces(self):
        for urlify in implementations:
            self.assertSequenceEqual(urlify([c for c in 'nospaces']), [c for c in 'nospaces'])


