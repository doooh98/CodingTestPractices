# input()은 한줄 입력 받음
# map()은 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용
# 개수가 많으면 list로 하고 개수가 적으면 a,b,c = map(int, input().split())
# 4개 인풋인데 a,b,c면 순서대로 담기고 마지막게 생략되는게 아니라 오류가 뜸.(개수 맞출것.)
# input()은 문자열로 받기 떄문에 int로 형변환을 시켜야함
# 고로 map(int, input())을 하는것임

# 받은 입력이
# 5
# 65 90 75 34 99
# 학생수와 점수 일경우

# 데이터 개수 입력
import sys
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)  # 내림차순
print(data)

print("---------------")
# 입력이 많거나 빠르게 받아야 할 경우
# sys.stdin.readline()사용
# 엔터는 줄바꿈 기호이므로 rstrip()사용하여 인식 안되도록 함


data = sys.stdin.readline().rstrip()
print(data)

# output
a = 1
b = 2
print(a, b)  # 1 2
print(7, end=" ")
print(8, end=" ")  # 7 8

print("나는 No." + str(a)+"이다")  # 7 8 나는 No.1이다

# f-string
print(f"나는 NO.{a}이다")  # 위와 같음.
