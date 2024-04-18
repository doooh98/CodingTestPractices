# even number of digits.
# A ticket number is considered lucky
# if the sum of the first half of the digits
# is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, true (1+2 = 3+0)
# For n = 239017, false.
def solution(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))
