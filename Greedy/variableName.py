# Correct variable names consist only of English letters,
# digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

# Example

# For name = "var_1__Int", the output should be
# solution(name) = true;
# For name = "qq-q", the output should be
# solution(name) = false;
# For name = "2w2", the output should be
# solution(name) = false.
def solution(name):
    return name.isidentifier()

# --------------------------------------------


def solution(name):
    if name[0].isdigit():
        return False
    for i in range(len(name)):
        if not (name[i].isdigit() or name[i].isalpha() or name[i] == "_"):
            return False
    return True
