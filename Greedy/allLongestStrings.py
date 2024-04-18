# Given an array of strings,
# return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"],
# solution(inputArray) = ["aba", "vcd", "aba"].
def solution(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r
