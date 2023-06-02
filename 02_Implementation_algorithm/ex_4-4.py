"""

문제 이름 : 게임 개발

핵심 : 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
->

"""
# 내 코드
import sys
map_size = list(map(int, sys.stdin.readline().rstrip().split(' ')))     # [세로길이(행), 가로길이(열)]
start = list(map(int, sys.stdin.readline().rstrip().split(' ')))        # [x, y, 방향]
direction = [0, 1, 2, 3]                                                # 방향 -> 0:북, 1:동, 2:남, 3:서
direction_add = [[-1, 0], [0, -1], [1, 0], [0, 1]]                      # 각 방향일 때 이동 경로
map_structure = []
for _ in range(map_size[0]):
    map_structure.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

next_direction = 0

for i in direction:         # 갈 곳 정하기
    if i == start[2]:
        next_direction_add = direction_add[i]
        #new_x =

# 책 코드
import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
d = [[0] * m for _ in range(n)]                             # 방문한 위치 저정할 zero matrix
x, y, direction = map(int, sys.stdin.readline().rstrip().split(' '))
d[x][y] = 1                                                 # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))     # 전체 맵 정보 입력 받기

dx = [-1, 0, 1, 0]              # 북, 동, 남, 서 방향 정의
dy = [0, 1, 0, -1]

def turn_left():            # 왼쪽으로 회전
    global direction        # 정수형 변수인 direction 변수가 함수 바깥에서 선언된 전역변수이므로
    direction -= 1
    if direction == -1:
        direction = 3       # 이런 식으로 0~3의 범위를 벗어날 때 다시 3으로 가도록 반복할 수 있음

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()                     # turn left
    nx = x + dx[direction]          # 한칸 전진 좌표 계산
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:   # 한칸 전진했을 때 (1)가본 적 없고 (2)육지면...
        d[nx][ny] = 1                           # 방문 처리
        x = nx                                  # 현재 좌표 업데이트
        y = ny
        count += 1                              # 방문 칸 수 증가
        turn_time = 0                           # turn time 초기화
        continue                                # 아래 코드 다 무시하고 while문 처음으로 돌아감
    else:                                       # 한칸 전진했을 때 가본 적 있거나, 바다면...
        turn_time += 1                          # turn time 증가하고 처음으로 돌아가거나 종료여부 결정

    if turn_time == 4:                          # 네번 돌게 되고...
        nx = x - dx[direction]                  # 방향 유지한 채로 한칸 후진 좌표 계산
        ny = y - dy[direction]
        if array[nx][ny] == 0:                  # 후진 시 육지면...
            x = nx                              # x, y 업데이트
            y = ny
        else:                                   # 후진 시 바다면...
            break                               # while문 종료
        turn_time = 0                           # 종료 안 되면 다시 while문 반복

print(count)
