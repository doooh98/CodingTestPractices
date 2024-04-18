i = 0
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

for x in [1, 2, 3, 4, 5]:
    print(x, end=" ")
print()

for i in range(10):
    print(i, end=" ")

result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue  # for문 시작지점으로 돌아감 (i++)
    result += i

print(result)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 0 apple
# 1 banana
# 2 cherry

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# 1 apple
# 2 banana
# 3 cherry

words = ["hello", "world", "python"]
for index, word in enumerate(words):
    if "o" in word:
        print(f"Index of '{word}': {index}")

for i in range(1, 10, 3):
    print(i)  # 1부터 9까지 3씩 뛰어감
for i in range(1, 10, -1):
    print(i)  # 1부터 9까지 역순으로
for i in range(10, -1, -1):
    print(i)  # 10부터 0까지 -1씩 뛰어감
