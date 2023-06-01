"""

문제 이름 : 상하좌우

핵심 : N*N 정사각형 공간을 벗어나는 움직임은 무시하는 것을 구현하는게 중요할 듯
->

"""
# 내 풀이
import sys
n = int(sys.stdin.readline().rstrip())
plans = list(sys.stdin.readline().rstrip().split(' '))

start_row = 1
start_column = 1

for i in plans:
    if i == 'R':
        if start_column == n:
            pass
        else:
            start_column += 1
    elif i == 'L':
        if start_column == 1:
            pass
        else:
            start_column -= 1
    elif i == 'U':
        if start_row == 1:
            pass
        else:
            start_row -= 1
    elif i == 'D':
        if start_row == n:
            pass
        else:
            start_row += 1
    else:
        pass

print(start_row, start_column)

# 책 풀이
n = int(input())
x, y = 1, 1
plans = input().split(' ')

dx = [0, 0, -1, 1]                  # L, R, U, D에 따른 이동 방향
dy = [-1, 1, 0, 0]                  # L, R, U, D에 따른 이동 방향
move_types = ['L', 'R', 'U', 'D']   # 이동 종류

for plan in plans:                      # 이동 계획 하나씩 살펴 봄
    for i in range(len(move_types)):    # 이번 계획은 L, R, U, D 중 어떤 것인지 확인
        if plan == move_types[i]:       # 만약 이번 계획을 파악했을 때,
            nx = x + dx[i]              # 계획에 따라 dx만큼 움직임
            ny = y + dy[i]              # 계획에 따라 dy만큼 움직임
        if nx < 1 or ny < 1 or nx > n or ny > n:    # 맵을 벗어나면...
            continue                                # x, y 업데이트 안 하고 다음 plan으로
        x, y = nx, ny                               # 맵을 벗어나지 않았으면... x, y를 nx, ny로 업데이트

print(x, y)