# DFS 기본 예제
graph = [
    [],
    [2, 3, 8],  # 1번 노드
    [1, 7],  # 2번 노드
    [1, 4, 5],  # 3번 노드
    [3, 5],  # 4번 노드
    [3, 4],  # 5번 노드
    [7],  # 6번 노드
    [2, 6, 8],  # 7번 노드
    [1, 7]  # 8번 노드
]

order = []
visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True
    order.append(v)
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return order

dfs(graph, 1, visited)

# ================================================================================================================= #

# BFS 기본 예제
from collections import deque

graph = [
    [],
    [2, 3, 8],      # 1번 노드
    [1, 7],         # 2번 노드
    [1, 4, 5],      # 3번 노드
    [3, 5],         # 4번 노드
    [3, 4],         # 5번 노드
    [7],            # 6번 노드
    [2, 6, 8],      # 7번 노드
    [1, 7]          # 8번 노드
]

visited = [False] * 9
order = []

def bfs(graph, v, visited):             # deque로 구현
    q = deque([v])
    visited[v] = True
    while q:
        next = q.popleft()
        order.append(next)
        for i in graph[next]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
    return order

def bfs(graph, v, visited):             # list로 구현
    q = [v]
    visited[v] = True
    while q:
        next = q[0]
        del q[0]
        order.append(next)
        for i in graph[next]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
    return order

bfs(graph, 1, visited)

# ================================================================================================================= #

# DFS 기본 문제
graph = []
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/Book_5_10.txt', 'r')
n, m = map(int, f.readline().rstrip().split(' '))
for _ in range(n):
    graph.append(list(map(int, f.readline().rstrip())))
f.close()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        for k in range(4):
            dfs(x + dx[k], y + dy[k])
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
          result += 1

print(result)

# ================================================================================================================= #

# BFS 기본 문제
from collections import deque
graph = []
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/Book_5_11.txt', 'r')
n, m = map(int, f.readline().rstrip().split(' '))
for _ in range(n):
    graph.append(list(map(int, f.readline().rstrip())))
f.close()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):                    # deque로 구현
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]

def bfs(x, y):                    # list로 구현
    q = [(x, y)]
    while q:
        x, y = q[0]
        del q[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))