"""

문제 이름 : 시각

핵심 : N*N 정사각형 공간을 벗어나는 움직임은 무시하는 것을 구현하는게 중요할 듯
->

"""
# 내 코드
import sys
n = int(sys.stdin.readline().rstrip())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            t = ''
            t += f'{i}' + ':' + f'{j}' + ':' + f'{k}'
            if '3' in t:
                count += 1

print(count)

# 책 코드 -> 계산량 더 줄임
import sys
n = int(sys.stdin.readline().rstrip())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):     # 여기서 시간 바로 만들고 조건문에 넣음으로써 시간을 줄일 수 있음
                count += 1

print(count)