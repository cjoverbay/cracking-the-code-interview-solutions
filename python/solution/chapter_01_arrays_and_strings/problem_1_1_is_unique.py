"""
Problem:
    Part I: Implement an algorithm to determine if a string has
            all unique characters.
    Part II: What if you cannot use additional data structures?
"""

import itertools


def all_unique(s):
    """
    Returns a boolean which is True if each element in
    iterable was used only once.

    >>> all_unique('abcd')
    True
    >>> all_unique('ab')
    False
    """
    seen_it = {}
    for c in s:
        if c in seen_it:
            return False
        else:
            seen_it[c] = True
    return True


# Time: O(n^2)  Space: O(1)
def all_unique_no_extra_space(s):
    """
    Returns a boolean which is True if each element in
    iterable was used only once.

    >>> all_unique('abcd')
    True
    >>> all_unique('aa')
    False
    """
    for i in range(len(s)):
        for j in itertools.chain(range(i), range(i+1, len(s))):
            if s[i] == s[j]:
                return False
    return True



