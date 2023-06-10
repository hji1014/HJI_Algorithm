"""
[적록색약]
"""
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