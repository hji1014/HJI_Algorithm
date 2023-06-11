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

# DFS 기본 문제 (음료수 얼려 먹기)
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

# BFS 기본 문제 (미로 탈출)
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

# DFS/BFS 문제 (BJ_1260, DFS와 BFS)
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

# DFS/BFS 문제 (BJ_2667, 단지번호붙이기)
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

# DFS 문제 (BJ_2606, 바이러스)
n = int(input())        # 컴퓨터의 수, 간선의 수
m = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)
order = []
def dfs(arr, v, visited):
    visited[v] = True
    order.append(v)
    for i in arr[v]:
        if visited[i] == False:
            dfs(arr, i, visited)
    return order

print(len(dfs(arr, 1, visited)) - 1)

# ================================================================================================================= #

# DFS/BFS 문제 (BJ_2606, 유기농 배추)
### DFS ###
import sys
sys.setrecursionlimit(10000)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split(' '))
    graph = [[0] * m for _ in range(n)]
    #f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1012.txt', 'r')
    for _ in range(k):
        #x, y = map(int, f.readline().rstrip().split(' '))
        x, y = map(int, input().split(' '))
        graph[y][x] = 1
    #f.close()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    group = 0

    def dfs(graph, a, b):
        if graph[a][b] == 1:
            graph[a][b] = 0
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if -1 < nx < n and -1 < ny < m:
                    #if graph[nx][ny] == 1:
                    #    graph[nx][ny] = 0
                    dfs(graph, nx, ny)
            return True
        else:
            return False

    for i in range(n):
        for j in range(m):
            if dfs(graph, i, j) == True:
                group += 1
    print(group)

# ********************************************************** #

### BFS ###

from collections import deque

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split(' '))
    graph = [[0] * m for _ in range(n)]
    #f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1012.txt', 'r')
    for _ in range(k):
        #x, y = map(int, f.readline().rstrip().split(' '))
        x, y = map(int, input().split(' '))
        graph[y][x] = 1
    #f.close()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    group = 0

    def bfs(graph, a, b):
        q = deque()
        q.append((a, b))
        while q:
            x, y = q.popleft()
            if graph[x][y] == 1:
                graph[x][y] = 0                 # 하나의 배추 집합을 모두 0으로 바꾸기(방문처리를 2로)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if -1 < nx < n and -1 < ny < m:
                        if graph[nx][ny] == 1:
                            q.append((nx, ny))


    for i in range(n):
        for j in range(m):
            #if bfs(graph, i, j) == True:
            if graph[i][j] == 1:
                bfs(graph, i, j)
                group += 1
    print(group)

# ================================================================================================================= #

# DFS 문제 (BJ_10026, 적록색약)
import sys
sys.setrecursionlimit(10000)

import copy

#n = int(input())
#graph = []
#for _ in range(n):
#    graph.append(list(input()))

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_10026.txt', 'r')
n = int(f.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(f.readline().rstrip()))
f.close()

normal = 0
abnormal = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n_graph = copy.deepcopy(graph)
a_graph = copy.deepcopy(graph)

for i in range(n):                  # 환자 그래프의 G원소를 R로 바꾸기
    for j in range(n):
        if a_graph[i][j] == 'G':
            a_graph[i][j] = 'R'

def n_dfs(x, y):      # 정상인 구역 카운팅
    start = n_graph[x][y]
    n_graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < n:
            if n_graph[nx][ny] == start:
                n_dfs(nx, ny)

def a_dfs(x, y):      # 환자 구역 카운팅
    start = a_graph[x][y]
    a_graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < n:
            if a_graph[nx][ny] == start:
                a_dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if n_graph[i][j] != 0:
            n_dfs(i, j)
            normal += 1

for i in range(n):
    for j in range(n):
        if a_graph[i][j] != 0:
            a_dfs(i, j)
            abnormal += 1

print(normal, abnormal)

# ================================================================================================================= #

# BFS 문제 (BJ_7569, 토마토)

from collections import deque

#m, n, h = map(int, input().split(' '))             # m : 열, n : 행, h : 높이
#graph = []
#for i in range(h):
#    mat_2 = []
#    for j in range(n):
#        mat_2.append(list(map(int, input().split(' '))))
#    graph.append(mat_2)

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_7569.txt', 'r')
m, n, h = map(int, f.readline().rstrip().split(' '))             # m : 열, n : 행, h : 높이
graph = []              # 인덱스 순서 : h, n, m
for i in range(h):
    mat_2 = []
    for j in range(n):
        mat_2.append(list(map(int, f.readline().rstrip().split(' '))))
    graph.append(mat_2)
f.close()

dx = [-1, 1, 0, 0, 0, 0]                # 방향 : 상, 하, 좌, 우, 위, 아래
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()                             # 순차적으로 하나씩 값 올려주면서 바꾸기 위해서는
for i in range(h):                      # -> 큐에 미리 1인 위치를 미리 담아두고 이후에 BFS를 수행하는 것이 핵심
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nz < h and -1 < nx < n and -1 < ny < m:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append((nz, nx, ny))      # 값 변경 전 값이 0인 위치를 저장

bfs()

impossible = False                          # 정답 출력
count = -1e9
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                impossible = True
                print(-1)
                exit(0)                             # 코드 강제 종료
            count = max(count, graph[i][j][k])

print(count - 1)

# ================================================================================================================= #

# BFS 문제 (BJ_16236, 아기 상어)
n = int(input())
space = []
for _ in range(n):
    space.append(list(map(int, input().split(' '))))

INF = 1e9
now_size = 2
now_x, now_y = 0, 0
dx = [-1, 1, 0, 0]                          # 이동할 수 있는 방향
dy = [0, 0, -1, 1]

for i in range(n):                          # 상어 위치 찾고 좌표 저장하고 아무것도 없는 것으로 초기화
    for j in range(n):
        if space[i][j] == 9:
            now_x, now_y = i, j
            space[now_x][now_y] = 0

# from collections import deque
def bfs():                                  # 모든 위치까지의 '최단 거리'만 계산하는 BFS 함수
    dist = [[-1] * n for _ in range(n)]     # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    q = [(now_x, now_y)]
    dist[now_x][now_y] = 0                  # 시작 위치는 도달이 가능하다고 보며 거리는 0
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
                    dist[nx][ny] = dist[x][y] + 1                        # 초기화 값이 -1이기 때문에 (?)
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

# ================================================================================================================= #

# DFS 문제 (BJ_19236, 청소년 상어)
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
                    if nx != now_x or ny != now_y:     # => if not (nx == now_x and ny == now_y):
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
