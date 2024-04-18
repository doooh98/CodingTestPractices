def add(a, b): return a + b


print(add(3, 7))

add(b=30, a=4)  # param직접지정도 가능

a = 10


def func():
    global a
    a += 1
    print(a)


def nonglobalfunc():
    a = 0  # a는 global a가 아닌 함수내부의 또 다른 a임
    a += 1
    print(a)


func()
nonglobalfunc()
print(a)

array = [1, 2, 3, 4]


def func2():
    print(a)  # global 없이 global a를 프린트함
    array.append(5)  # 전역변수참조
    print(array)


def func3():
    array = [3, 4]  # 이름같을경우 내부변수 참조
    print(array)


def func4():
    global array
    array = [9, 10]  # 전역변수 array를 바꿈


func2()
func3()
print(array)
func4()
print(array)

# 여러값 반환


def various(a, b):
    first = a+b
    second = a - b
    third = a * b
    return first, second, third


a, b, c = various(3, 2)
print(a, b, c)


# 람다 공부 따로하기
# 람다란, 파이프와 비슷하게 작용하는 요약형 함수이다
def add(x, y): return x+y


# add 라는 함수에 param은 x, y이며 기능은 x+y이다
print(add(3, 4))
# list함수도 가능하다
lambdas = [lambda x:x + 10, lambda x:x+20]
print(lambdas[0](2) + lambdas[1](2))  # 34
print(f"{lambdas[0](2)} + {lambdas[1](2)}")  # 12+22
