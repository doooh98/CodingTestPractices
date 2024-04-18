# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# solution(inputArray) = 3.

import math


def solution(inputArray):
    return max(abs(inputArray[i] - inputArray[i+1]) for i in range(len(inputArray)-1))
