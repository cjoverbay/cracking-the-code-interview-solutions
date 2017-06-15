"""
Problem: 1.2 Given two strings, write a method to decide if one
         is a permutation of the other
"""


# Time complexity: O(len(s1) + len(s2))
# Space complexity: O(len(s1) + len(s2)) or O(1) if fixed char set
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}

    for c in s1:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    for c in s2:
        if c in char_count:
            char_count[c] -= 1
        else:
            return False

    return all(v == 0 for v in char_count.values())
