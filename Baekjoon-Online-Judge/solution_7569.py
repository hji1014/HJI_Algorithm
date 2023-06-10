"""
[토마토]
"""
# 내 풀이
"""
틀린 이유 :
"""
m, n, h = map(int, input().split(' '))             # m : 열, n : 행, h : 높이
graph = []
for i in range(h):
    mat_2 = []
    for j in range(n):
        mat_2.append(list(map(int, input().split(' '))))
    graph.append(mat_2)

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

def bfs(z, x, y):       # 한 번 돌아가면 다 익어버림 / 최소 일 수 못 구하겠음
    q = [[z, x, y]]
    while q:
        z, x, y = q[0][0], q[0][1], q[0][2]
        del q[0]
        if graph[z][x][y] == 1:
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nz < h and -1 < nx < n and -1 < ny < m:
                    if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = 1
                        q.append([nz, nx, ny])
    return print(graph)


for i in range(h):                          # bfs 수행
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                bfs(i, j, k)

for i in range(h):                          # 정답 출력
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                impossible = True
if count == 0:
    if impossible:
        print(-1)
    else:
        print(0)
else:
    print(count)

# ================================================================================================================= #

# 블로그 풀이
"""
ref : https://resilient-923.tistory.com/263
"""
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
