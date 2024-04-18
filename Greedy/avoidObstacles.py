# You are given an array of integers representing
# coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point
# with coordinate 0 to the right.
# You are allowed only to make jumps
# of the same length represented by some integer.

# Find the minimal length of the jump enough
# to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# solution(inputArray) = 4. (0* 12 3 *4* 5 6 7 *8* 9)

def solution(inputArray):
    inputArray.sort()
    if len(inputArray) == 0:
        return 0
    elif len(inputArray) == 1:
        return inputArray[0] + 1

    for r in range(1, inputArray[-1] + 1):
        if all(k % r != 0 for k in inputArray):
            return r
    return inputArray[-1] + 1
