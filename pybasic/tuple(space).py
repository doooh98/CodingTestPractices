# list (static list = tuple)
# space complexity ^ 수정불가

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(a[3])
print(a[1:4])

# 최단경로 알고리즘
# 데이터 나열을 해싱의 "키값"으로 사용할때
# 메모리 딸릴때

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]
# lambda 매개변수 : 표현식


print(sorted(array, key=my_key))
# [('이순신',32),('홍길동',50),('아무개', 74)]
print(sorted(array, key=lambda x: x[1]))
# [('이순신',32),('홍길동',50),('아무개', 74)]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))
# [7,9,11,13,15]

words = ["hello", "world", "python"]
lengths = map(len, words)

print(list(lengths))
# 출력: [5, 5, 6]


# almostIncreasingSequence참조
a = [1, 2, 3, 4, 5, 6]

# (1,2,3),(2,3,4),(3,4,5),(4,5,6),(5,6,100000)
b = zip(a, a[1:], a[2:]+[10**6])
# zip() 함수는 이 세 리스트의 동일한 인덱스에 위치한 요소들을 묶어서 튜플로 만듭니다
s = [1, 2, 3, 1]

# return
3 > sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10**6]))
# for 의 각 i,j,k가 zip으로 만들어진 튜플의 각 element가 됨
# 1st for loop
# i = 1, j = 2, k = 3, i<j, j<k so none add on the sum
# 2nd for loop
# i = 2, j = 3, k = 1, i < j, j > k so 1 add on the sum
# 3rd for loop
# i = 3, j = 1, k = 100000, i > j so 1 add on the sum
# thus sum = 2, true
