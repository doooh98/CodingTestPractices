# 집합 = 중복 미허용, 순서 x
# 리스트나 문자열로 초기화가능(set함수 사용해야함)
# {}안에 각 원소를 , 기준으로 구분하여 삽입함으로서 초기화 가능
# 데이터 조회 수정 O1

# 합,교,차 집합 사용가능

data = set([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
print(data)  # 중복 삭제됨

data = {1, 1, 2, 3, 4, 4, 5}
print(data)  # 위와 동일

print("--------------")
# 문법
data = set([1, 2, 3])
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)

# return {a, b} == {c, d}
# (a == c or a == d) and (b == c or b == d)

# {} is for defining set or dict
