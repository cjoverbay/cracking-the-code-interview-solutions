"""
Problem: 1.3 Write a method to replace all spaces in a string with '%20'
         You may assume that the string has sufficient space at the end
         to hold the additional characters, and that you are given the "true"
         length of the string
"""


# Note that strings are immutable in python, so we will use character
# lists to do this problem.  Note that the input list should have additional
# spaces at the end.
def urlify(c_arr):
    # Move from right to left swapping values into rightful place
    # and inserting %20 when needed

    # Find meaningful end to string (last non space character)

    i = len(c_arr) - 1
    while i >= 0 and c_arr[i] == ' ':
        i -= 1
    end_idx = i

    # Count meaningful spaces (non trailing spacses)
    space_count = 0
    while i > 0:
        i-=1
        if c_arr[i] == ' ':
            space_count += 1

    # while a space is a single character, '%20' has three
    # so the new end to the string will be extended by two
    # for each space that we are replacing
    to_place_idx = end_idx + space_count * 2
    i = end_idx
    while i >= 0:
        if c_arr[i] == ' ':
            c_arr[to_place_idx] = '0'
            c_arr[to_place_idx - 1] = '2'
            c_arr[to_place_idx - 2] = '%'
            to_place_idx -= 3
        else:
            c_arr[to_place_idx] = c_arr[i]
            to_place_idx -= 1
        i -= 1

    return c_arr
