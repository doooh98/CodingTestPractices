# Given an array of equal-length strings,
# you'd like to know if it's possible to
# rearrange the order of the elements
# in such a way that each consecutive pair
# of strings differ by exactly one character.
# Return true if it's possible, and false if not.

# Note: You're only rearranging the order of the strings,
# not the order of the letters within the strings!

# Example

# For inputArray = ["aba", "bbb", "bab"],
# solution(inputArray) = false.

# There are 6 possible arrangements for these strings:

# ["aba", "bbb", "bab"]
# ["aba", "bab", "bbb"]
# ["bbb", "aba", "bab"]
# ["bbb", "bab", "aba"]
# ["bab", "bbb", "aba"]
# ["bab", "aba", "bbb"]
# None of these satisfy the condition of consecutive strings differing by 1 character,
# so the answer is false.

# For inputArray = ["ab", "bb", "aa"], the output should be
# solution(inputArray) = true.

# It's possible to arrange these strings
# in a way that each consecutive pair of strings differ by 1 character
# (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

def solution(inputArray):
    n = len(inputArray)

    # Helper function to determine if two strings differ by exactly one character
    def differ_by_one(s1, s2):
        count_diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count_diffs += 1
            if count_diffs > 1:
                return False
        return count_diffs == 1

    # Build the graph as adjacency list
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if differ_by_one(inputArray[i], inputArray[j]):
                graph[i].append(j)
                graph[j].append(i)

    # Check if there's a Hamiltonian path in the graph
    def find_path(start, path):
        if len(path) == n:
            return True
        for neighbor in graph[start]:
            if neighbor not in path:
                path.append(neighbor)
                if find_path(neighbor, path):  # back tracking
                    return True
                path.pop()
        return False

    # Try to find a Hamiltonian path starting from each vertex
    for i in range(n):
        if find_path(i, [i]):
            return True
    return False
