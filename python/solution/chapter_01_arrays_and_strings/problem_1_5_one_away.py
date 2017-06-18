"""
Problem: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character.
    Given two strings, write a function to check if they are one
    edit (or zero edits) away.
"""


# This implementation is O(n) in time, and O(1) in space
def check_one_away(str1, str2):
    """
    Returns a boolean which is True if the strings
    are within a single character edit away
    (Remove, Insert, Replace)

    >>> check_one_away('pale','ple')
    True
    >>> check_one_away('pales', 'pale')
    True
    >>> check_one_away('pale', 'bale')
    True
    >>> check_one_away('pale', 'bake')
    False
    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    edit_required = False
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edit_required:
                return False
            edit_required = True

            # Find what kind of edit is required
            if (i+1) < len(str1) and str1[i+1] == str2[j]:
                i += 1
            elif (j+1) < len(str2) and str2[j+1] == str1[i]:
                j += 1
        i += 1
        j += 1
    return True
