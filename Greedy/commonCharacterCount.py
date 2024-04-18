# Given two strings,
# find the number of common characters between them.

# Example
# s1 = "aabcc" and s2 = "adcaa"  = 3(a,a,c).

def solution(s1, s2):
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))
