"""
[알파벳]
"""
r, c = map(int, input().split(' '))
graph = []
for _ in range(r):
    graph.append(list(input()))

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1987.txt', 'r')
r, c = map(int, f.readline().split(' '))
graph = []
for _ in range(r):
    graph.append(list(f.readline().rstrip()))
for i in range(r):
    for j in range(c):
        num = (ord(graph[i][j]) - 65) % 26
        graph[i][j] = num
f.close()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [False] * 26

def dfs(x, y):
    #visited[graph[x][y]] = True
    graph[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < r and -1 < ny < c:
            if visited[graph[nx][ny]] != True:
                if graph[nx][ny] != -1:
                    #visited[graph[nx][ny]] = True
                    graph[nx][ny] = -1
                    dfs(nx, ny)

dfs(0, 0)


# 블로그 풀이
#r, c = map(int, input().split(' '))
#graph = []
#for _ in range(r):
#    graph.append(list(input()))

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1987.txt', 'r')
r, c = map(int, f.readline().split(' '))
graph = []
for _ in range(r):
    graph.append(list(f.readline().rstrip()))

ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < r and -1 < ny < c and graph[nx][ny] not in alphas:
            alphas.add(graph[nx][ny])           # set에 원소 추가할 때 add() 함수 사용
            dfs(nx, ny, count + 1)
            alphas.remove(graph[nx][ny])        # 해당 경로가 이제 막히면 지워주는게 포인트

alphas.add(graph[0][0])
dfs(0, 0, 1)
print(ans)