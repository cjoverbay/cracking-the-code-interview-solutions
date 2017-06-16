"""
Problem: Permutation: Given a string, write a function to check
         if it is a permutation of a palindrome. A palindrome
         is a word or phrase that is the same forwards and backwards.
         A permutation is a rearrangement of letters. The palindrome
         does not need to be limited to just dictionary words.
"""


# This implementation is O(n) in time and space.
# If the character count is limited, space is O(len(unique_characters))
def is_perm_palindrome(s):
    """
    Returns a boolean which is True if the string
    is a permutation of a palindrome

    >>> is_perm_palindrome('Tact Coa')
    True`
    Taco Cat

    >>> is_perm_palindrome('ab')
    False
    """
    matches = {}

    for c in s:
        if c != ' ':
            l = c.lower()
            if l in matches:
                matches[l] = not matches[l]
            else:
                matches[l] = False

    unmatched = 0
    for match in matches.values():
        if not match:
            unmatched += 1

    return unmatched <= 1
