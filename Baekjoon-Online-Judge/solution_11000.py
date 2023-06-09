"""
[강의실 배정]
"""

# 내 풀이
"""
틀린 이유 : 
"""

"""
# 1
import sys
n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

# 2
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split(' '))))
"""

# 3
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_11000.txt')
n = int(f.readline().rstrip())
data = []
for _ in range(n):
    data.append(list(map(int, f.readline().rstrip().split(' '))))
f.close()

data.sort(key=lambda x : x[1])
data.sort(key=lambda x : x[0])

room = 1
now_time = -1
times = []

for a, b in data:
    if a >= now_time:
        next_time = b
        if next_time >= now_time:
            now_time = next_time

    else:
        room += 1
        #next_time = b
        #if next_time >= now_time:
        #    now_time = next_time

# 블로그 풀이
"""
ref : https://hongcoding.tistory.com/79, https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
"""
from collections import deque

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split(' '))))

room = deque()
room.append(data[0][1])
