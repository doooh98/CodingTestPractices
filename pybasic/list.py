a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[3])  # 4
a = [0] * 10  # 0을 10개만큼 넣음
print(a)
a = [0] * 5  # 0을 5개만큼 넣고 뒤에 삭제
print(a)
a = [0] * 15  # 0을 15개만큼 넣음(늘림)
print(a)
# indexing
a[3] = 3  # 4번째자리
print(a)
a[-1] = -1  # 뒤에서 첫번째
print(a)
# slicing
print(a[0:5])  # 첫 5개 (0부터 4까지 (5전까지))
# list comprehension
arr = [i for i in range(10)]
print(arr)
del arr[3]

# 홀수만포함
arr = [i for i in range(20) if i % 2 == 1]
print(arr)

# 제곱
arr = [i*i for i in range(10)]
print(arr)

# 2차원 리스트 초기화 (3*4) (_ 는 변수없이 반복하고 싶을때)
arr = [[0]*3 for _ in range(4)]
print(arr)

# array creating value"1" in every 3x3 cells
# you can put equation for ex, i*j in "1"'s spot to change the value
array_3x3 = [[1 for _ in range(3)] for _ in range(3)]
print(array_3x3)


a = [1, 7, 9, 3, 5, 4, 2]
a.append(8)  # O1
print(a)

a.sort()  # Onlogn
print(a)

a.sort(reverse=True)  # On
print(a)
a.reverse()  # On
print(a)
print("------")
a.insert(4, "b")  # On
print(a)

print(a.count("b"))  # On

a.remove("b")  # On
print(a)

a.append(1)
a.append(1)
a.append(1)
remove_set = {1, 2, 3, 4}
result = [i for i in a if i not in remove_set]
print(result)

# slice 표현식 [::] (string도 list 인거 잊지말기)
# [start:stop:step]
inputString = "hello"
reverseString = inputString[::-1]
print(reverseString)
