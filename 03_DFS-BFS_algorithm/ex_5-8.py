"""

문제 이름 : DFS 예제

핵심 : stack 자료구조 사용, 재귀 함수 사용
-> 내가 이해한 방식은 dfs() 내부 재귀함수를 부르는 for문에서 점점 더 깊은 차원으로 들어갔다가
   인접 노드가 없으면 한 차원씩 위로 다시 올라오는 느낌.
   내 느낌이 맞길.

"""
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')           # end=' '로 인해 print할 때마다 다른 줄이 되는 것이 아니고 한 칸 띄어서 나오는 것
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
