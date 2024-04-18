# integers
a = 1000
b = -7
c = 0

print(a)

a += 3

print(a)

a = 1000.
print(a)  # 1000.0

a = -123.123
a = 123.123
a = -.2  # -0.2

a = 1e3  # 1000.0
print(a)

a = 1e9  # 1억.0 (무한값으로 활용 (최대값계산 등등))(실수형)
print(a)
a = int(1e9)  # 1억 (정수형)
# 실수형은 2진수체제인 컴퓨터에서 오류발생률이 높음 (정확도-)(float쓰기)

a = 0.3 + 0.6
print(a)
if a == 0.9:
    print(True)
else:
    print(False)

a = 123.456
print(round(a, 2))  # 10^-2에서 반올림, .0자리는 0

## "/"는 결과를 실수형으로 표기함 ##

a = "12a"
print(a.isdigit())


# 모든 숫자가 양수인지 검사
numbers = [1, 2, 3, 4, 5]
print(all(num > 0 for num in numbers))  # 출력: True

# 모든 단어가 특정 길이 이상인지 검사
words = ["apple", "banana", "cherry"]
print(all(len(word) >= 5 for word in words))  # 출력: True

str(1234)  # 숫자를 글자로 형변환
