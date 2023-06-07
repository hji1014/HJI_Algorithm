"""
[아기 상어]
ref :
"""

n = int(input())
space = []
for _ in range(n):
    space.append(list(map(int, input().split(' '))))

INF = 1e9
now_size = 2
now_x, now_y = 0, 0
dx = [-1, 1, 0, 0]                          # 이동할 수 있는 방향
dy = [0, 0, -1, 1]

for i in range(n):                          # 상어 위치 찾고 저장하고 아무것도 없는 것으로 초기화
    for j in range(n):
        if space[i][j] == 9:
            now_x, now_y = i, j
            space[now_x][now_y] = 0

def bfs():                                  # 모든 위치까지의 '최단 거리'만 계산하는 BFS 함수
    dist = [[-1] * n for _ in range(n)]     # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    q = [(now_x, now_y)]
    dist[now_x][now_y] = 0                  # 시작 위치는 도달이 가능하다고 보며 거리는 0
    # from collections import deque
    # q = deque([(now_x, now_y)])
    while q:
        x, y = q[0][0], q[0][1]
        del q[0]
        # x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if dist[nx][ny] == -1 and space[nx][ny] <= now_size:     # 자신의 크기와 같거나 작은 경우에 지나갈 수 있음
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist     # 모든 위치까지의 최단 거리 테이블 반환

def find(dist):                             # 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and space[i][j] >= 1 and space[i][j] < now_size:       # 도달이 가능하면서 먹을 수 있는 물고기일 때
                if dist[i][j] < min_dist:   # 가장 가까운 물고기 한 마리 선택 -> 중복 시 자동으로 상단 좌측부터 탐색하는 것
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0          # 최종 걸리는 시간
ate = 0             # 현재 크기에서 먹은 양
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        space[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
