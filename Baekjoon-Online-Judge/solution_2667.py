"""
[단지번호붙이기]
ref : https://hongcoding.tistory.com/71
"""

# DFS로 풀기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

        # 다양한 입력 방법들
#import sys
#n = int(sys.stdin.readline().rstrip())
#graph = []
#for _ in range(n):
#    graph.append(list(map(int, sys.stdin.readline().rstrip())))

#f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2667.txt', 'r')
#n = int(f.readline().rstrip())
#graph = []
#for i in range(n):
#    graph.append(list(map(int, f.readline().rstrip())))
#f.close()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global count                  # 전역 변수로 설정 안 하면 에러 발생 / 리스트 자료형 사용하면 전역 변수로 선언 안 해도 됨
        count += 1
        graph [x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    else:
        return False

count = 0
result = 0
house_num = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            house_num.append(count)
            result += 1
            count = 0

house_num.sort()
print(result)
for i in house_num:
    print(i)

# ================================================================================================================= #


# BFS로 풀기
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2667.txt', 'r')
n = int(f.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, f.readline().rstrip())))
f.close()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
    queue = []
    queue.append((a, b))
    graph[a][b] = 0             # 처음 시작하는 위치를 0으로 바꾸기
    count = 1                   # 처음 시작하는 곳부터 세기
    # n = len(graph)

    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

house_num = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_num.append(bfs(graph, i, j))

house_num.sort()
print(len(house_num))
for i in house_num:
    print(i)
