# hash table
# key, value
# key = immutable
# 순차적으로 저장하지않음 (순서 x) != list, tuple
# 데이터 조회 수정 O1

data = dict()
data['key'] = 'Value'
data['0964'] = 'correct'
data['사과'] = 'Apple'

print(data)

if '사과' in data:
    print('사과를 키값으로 갖고있는 데이터 존재함.')

# 키랑 값 데이터 따로 뽑기 가능 (형변환 필요)
key_list = data.keys()  # 키만보여줌
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
# 다른 형변환 (리스트로만 뽑을때)
key_list = list(data.keys())
print(key_list)

# 특정데이터
print(data['0964'])

n = 3
graph = {i: [] for i in range(n)}
# 0부터 2까지
# {0: [], 1: [], 2: []}
