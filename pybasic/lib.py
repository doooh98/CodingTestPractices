
import math
from collections import Counter  # counter
from itertools import permutations  # itertools
from itertools import product
from itertools import combinations_with_replacement

# 내장함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공합니다.
# 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있습니다.

# sum()

result = sum([1, 2, 3, 4, 5])
print(result)  # 15

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)  # 2 7

# eval()
result = eval("(3+5)*7")
print(result)  # 56

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)  # [1,4,5,8,9]
print(reverse_result)  # [9,8,5,4,1]

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)  # [('이순신',75),('아무개',50),('홍길동',35)]

# itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공합니다.
# 특히 순열과 조합 라이브러리는 코딩 데이터에서 자주 사용됩니다.
# 순열:서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# {'A','B','C'}에서 세 개를 선택하여 나열하는 경우: 'ABC', 'ACB, 'BAC', 'BCA', 'CAB', 'CBA'
# 조합: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# {'A','B','C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우: 'AB', 'AC', 'BC'
# 순열의 수: nPr = n * (n-1)*(n-2)*...*(n-r+1)
# 조합의 수: nCr = (n*(n-1)*(n-2)*...*(n-r+1))/r!


data = ['A', 'B', 'C']  # 데이터 준비

result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)
# [('A','B','C'), (...'ACB, 'BAC', 'BCA', 'CAB', 'CBA'...]

data = ['A', 'B', 'C']  # 데이터 준비

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)


data = ['A', 'B', 'C']  # 데이터 준비

result = list(combinations_with_replacement(
    data, 2))  # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)


# heapq: 힙(Heap) 자료구조를 제공합니다
# 일반적으로 우선순위 큐 기능을 구현하기 위해 사용됩니다.

# bisect:이진 탐색(Binary Search)기능 제공

# collections: deque, Counter(횟수 세는 기능)등 유용한 자료구조 포함
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력, 3
print(counter['green'])  # 'green'이 등장한 횟수 출력, 1
print(dict(counter))  # 사전 자료형으로 반환, {'red':2,'blue':3,'green':1}


# math: 필수적인 수학적 기능을 제공합니다.
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함합니다.


# 최소 공배수 (LCM)를 구하는 함수
def lcm(a, b):
    return a*b // math.gcd(a, b)


a = 21
b = 14
print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산, 7
print(lcm(21, 14))  # 최소 공배수(LCM) 계산, 42

math.ceil(1.2)  # 2
math.ceil(1.8)  # 2
print(math.ceil(-1.2))  # -1
