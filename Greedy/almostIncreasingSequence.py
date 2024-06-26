# Given a sequence of integers as an array,
# determine whether it is possible to obtain a strictly
# increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a
# strictly increasing if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.

# Example

# For sequence = [1, 3, 2, 1] = false. ("2" and "1" which is more than one)
# For sequence = [1, 3, 2] = true. (only "3" needed to be deleted)

def solution(s):
    return 3 > sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10**6]))
