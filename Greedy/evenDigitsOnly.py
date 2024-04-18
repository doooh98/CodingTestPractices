# Check if all digits of the given integer are even.

# Example

# For n = 248622, the output should be
# solution(n) = true;
# For n = 642386, the output should be
# solution(n) = false.
def solution(n):
    while (n > 0):
        if (n % 10) % 2 == 1:
            return False  # 마지막 자릿수를 리스트에 추가
        n //= 10  # 숫자에서 마지막 자릿수 제거
    return True
