x = 15

if x >= 10:
    print("x>=10")

if x >= 0:
    print("x>=0")
    if x >= 20:  # 들여쓰면 내부에서 실행
        print("x>=20&x>=0")
elif x == -1:
    print("neg")
else:
    print("nothin")

if x >= 30:
    print("x>=30")

if True or False:
    print("True")
if True and False:
    print("False")
if not False:
    print("True")

# in, not in

a = [1, 2, 3]
if 1 in a:
    print("1")
if 4 not in a:
    print("4 not in a list")

# if~else
result = "success" if 1 in a else "Fail"
print(result)

# 대수학
x = 2
if 0 < x < 20:
    print("wow")
