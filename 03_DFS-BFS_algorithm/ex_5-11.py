"""

문제 이름 : 미로 탈출

핵심 : 최단거리 -> BFS

"""
# 책 풀이
from collections import deque

n, m = map(int, input().split(' '))
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]      # 이동할 네 방향 정의(상, 하, 좌, 우)
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))                                    # 시작 위치를 큐에 넣기
    while queue:                                            # 큐가 빌 때까지 반복
        x, y = queue.popleft()                              # 가장 먼저 들어간 큐 원소 뽑기
        for i in range(4):                                  # 현재 위치에서 네 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:      # 맵에서 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0:                          # 괴물이 있을 경우 무시
                continue
            if graph[nx][ny] == 1:                          # 해당 노드를 처음 방문하는 경우에 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1             # 순번 기록
                queue.append((nx, ny))                      # 큐에 넣기
    return graph[n - 1][m - 1]                              # 큐가 비었을 때 최단 거리 반환

print(bfs(0, 0))
