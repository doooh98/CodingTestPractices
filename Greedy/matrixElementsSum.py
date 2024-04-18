# # CodeBots are quite superstitious,
# # they refuse to stay in any of the free rooms,
# # or any of the rooms below any of the free rooms.

# # Given matrix, a rectangular matrix of integers,
# # where each value represents the cost of the room,
# # your task is to return the total sum of all rooms
# # that are suitable for the CodeBots
# # (ie: add up all the values that don't appear below a 0).

# Example

# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]
# answer = 9. (1+1+2+5)

# matrix = [[1, 1, 1, 0],
#           [0, 5, 0, 1],
#           [2, 1, 3, 10]]
# answer = 9 (1+1+1+5+1)

def solution(m):
    row = len(m)
    column = len(m[0])
    total = 0
    for j in range(column):
        for i in range(row):
            if m[i][j] != 0:
                total += m[i][j]
            else:
                break
    return total
