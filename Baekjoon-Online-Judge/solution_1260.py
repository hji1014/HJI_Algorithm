"""

[DFS와 BFS]

- 문제 설명
: 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가
작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

- 입력
: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

- 출력
: 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

"""
# 내 풀이
"""
틀린 이유 : 입력을 그래프로 구현하는 것에서 막힘
"""
n, m, v = map(int, input().split(' '))

# =================================================================================================== #

# 블로그 풀이
n, m, v = map(int, input().split(' '))

graph = [[] for _ in range(n + 1)]
for i in range(m):                                  # 그래프 만들기
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()

def dfs(graph, v, visited1):
    visited1[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited1[i]:
            dfs(graph, i, visited1)

def bfs(graph, v):
    need_visited, visited2 = [], []
    need_visited.append(v)
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        if node not in visited2:
            visited2.append(node)
            need_visited.extend(graph[node])
    for i in range(len(visited2)):
        print(visited2[i], end=' ')


visited1 = [False] * (n + 1)
dfs(graph, v, visited1)
print()
bfs(graph, v)