# Two arrays are called similar
# if one can be obtained from another
# by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

# Example

# For a = [1, 2, 3] and b = [1, 2, 3] = true.

# For a = [1, 2, 3] and b = [2, 1, 3] = true.by swapping 2 and 1 in b.

# For a = [1, 2, 2] and b = [2, 1, 1] = false.

from collections import Counter as C


def solution(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3
