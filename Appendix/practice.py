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

# ================================================================================================================= #

# DFS/BFS 문제 (BJ_1260)
n, m, v = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

visited = [False] * (n + 1)                         ### DFS ###
order = []
#order = 0
def dfs(graph, v, visited):
    visited[v] = True
    order.append(v)
    # 전역 변수로 쓰는 경우
    #global order
    #order += 1
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return order

dfs(graph, v, visited)

from collections import deque                       ### BFS ###
def bfs(graph, v):
    need_visited, visited = deque([]), []
    need_visited.append(v)
    while need_visited:
        node = need_visited.popleft()
        #del need_visited[0]
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

bfs(graph, v)

# ================================================================================================================= #

# DFS/BFS 문제 (BJ_2667)
#n = int(input())
#graph = []
#for i in range(n):
#    graph.append(list(map(int, input())))

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2667.txt', 'r')
n = int(f.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, f.readline().rstrip())))
f.close()

count = 0
complex_num = 0
house_num = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):                                                  ### DFS ###
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    else:
        return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            complex_num += 1
            house_num.append(count)
            count = 0

from collections import deque                                   ### BFS ###
def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_num.append(bfs(i, j))

# ================================================================================================================= #

# BFS 문제 (BJ_16236)

