# Find the leftmost digit that occurs in a given string.

# Example

# For inputString = "var_1__Int", the output should be
# solution(inputString) = '1';
# For inputString = "q2q-q", the output should be
# solution(inputString) = '2';
# For inputString = "0ss", the output should be
# solution(inputString) = '0'.
import re


def solution(inputString):
    for i in inputString:
        if i.isdigit():
            return i
    return 0


# ------------


def solution(inputString):
    return re.findall('\d', inputString)[0]
