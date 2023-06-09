"""
[청소년 상어]
ref : 책
"""

# 내 풀이
"""
틀린 이유 : k를 직접 설정하고, i와 j를 직접 설정한 후 d = ... 줄부터 실행하면 하나씩 잘 이동하는데 왜 for문을 한 번에 돌리면 인덱스 에러가 나는지?
"""
arr = []
for _ in range(4):
    arr.append(list(map(int, input().split(' '))))
    #arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))

arr = []
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_19236.txt', 'r')
for _ in range(4):
    arr.append(list(map(int, f.readline().rstrip().split(' '))))
f.close()

space = []
for i in range(4):
    partial = []
    for j in range(8):
        if j % 2 == 0:
            partial.append([arr[i][j], arr[i][j + 1]])
    space.append(partial)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
result = 0
shark_num = 17
INF = 1e9

def shark_in(space):
    global result
    result += space[0][0][1]
    space[0][0] = (shark_num, space[0][0][1])
    return space
shark_in(space)

def fish_mov(space):
    for k in range(1, 17):
        for i in range(4):
            for j in range(4):
                if space[i][j][0] == k:
                    d = space[i][j][1] - 1
                    for l in range(8):              # 방향 확인
                        d_test = (d + l) % 8
                        nx = i + dx[d_test]
                        ny = j + dy[d_test]
                        if space[nx][ny][0] != 17 and -1 < nx < 4 and -1 < ny < 4:
                            temp = space[nx][ny]
                            break
                        else:
                            d_test += 1
                            nx = INF                        # 8개 방향 중에 없으면
                            ny = INF
                    if nx != INF and ny != INF:             # 이동
                        if space[nx][ny] != [0, 0]:         # 빈칸이 아니면 값 바꾸기
                            space[nx][ny] = space[i][j]
                            space[nx][ny][1] = d_test + 1   # 튜플 원소 바꿀 수 없음 -> 애초에 받을 때 리스트로 받아야 함
                            space[i][j] = temp
                        elif space[nx][ny] == [0, 0]:       # 빈칸이면 그냥 이동
                            space[nx][ny] = space[i][j]
                            space[i][j] = [0, 0]
                        #nx = 0
                        #ny = 0
                        #temp = [0, 0]
                    elif nx == INF and ny == INF:
                        #nx = 0
                        #ny = 0
                        #temp = [0, 0]
                        pass
    return space
fish_mov(space)

# ================================================================================================================= #


# 책 풀이
import copy

array = [[None] * 4 for _ in range(4)]
#f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_19236.txt', 'r')
for i in range(4):
    data = list(map(int, input().split(' ')))
    #data = list(map(int, f.readline().rstrip().split(' ')))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]
#f.close()

dx = [-1, -1, 0, 1, 1, 1, 0, -1]        # 8가지 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0              # 최종 결과

def turn_left(direction):                   # 현재 위치에서 왼쪽으로 회전된 결과 반환
    return (direction + 1) % 8

def find_fish(array, index):                             # 현재 배열에서 특정한 번호의 물고기 위치 찾기
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if -1 < nx < 4 and -1 < ny < 4:         # 맞나?
                    if nx != now_x or ny != now_y:     # = if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]     # 따로 저장 해놓고 바꾸지 않고 바로 바꿀 수 있음
                        break
                direction = turn_left(direction)

def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if -1 < now_x < 4 and -1 < now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result       # 밖에 있는 변수를 가져다 쓰는 것이기 때문에 전역변수로 설정
    array = copy.deepcopy(array)        # 이유는?

    total += array[now_x][now_y][0]     # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1         # 물고기를 먹었으니 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)                        # 물고기 이동

    positions = get_possible_positions(array, now_x, now_y)     # 상어 이동 가능 위치 찾기
    if len(positions) == 0:                                     # 이동할 수 있는 위치 없다면
        result = max(result, total)                             # 최댓값 저장
        return
    for next_x, next_y in positions:                            # 이동할 수 있는 모든 위치로 재귀적으로 탐색
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)
