"""
[좌표 압축]
"""
# 내 풀이 (시간 초과)
n = int(input())
data = list(map(int, input().split()))

convert = []
for i in range(len(data)):
    now = data[i]
    small_num = set()
    for j in data:
        if j < now:
            small_num.add(j)
    print(len(small_num), end=' ')

# 내 풀이 (시간 초과)
n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(data)

for i in range(len(data)):
    now = data[i]
    small_num = set()
    for j in sorted_data:
        if j < now:
            small_num.add(j)
        else:
            break
    print(len(small_num), end=' ')

# 내 풀이 (시간 초과)
import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_data_set = sorted(set(data))

for i in range(len(data)):
    now = data[i]
    ans = 0
    for j in sorted_data_set:
        if j < now:
            ans += 1
        else:
            break
    print(ans, end=' ')

# 내 풀이 (블로그에서 좌표 압축 개념 공부)
"""

좌표 압축 : 여러 곳에 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것
(작은 값부터 시작해서 0부터 인덱스를 부여하는 방식이다.)

[1, 10, 10000, 1000000] -> 좌표를 압축하여 순서대로 표현 -> [0, 1, 2, 3]


"""
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_data_set = sorted(set(data))

num_dict = {}
for i in range(len(sorted_data_set)):
    num_dict[sorted_data_set[i]] = i
for i in data:
    print(num_dict[i], end=' ')
