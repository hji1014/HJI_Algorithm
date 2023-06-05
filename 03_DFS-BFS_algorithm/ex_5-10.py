"""

문제 이름 : 음료수 얼려 먹기

핵심 :
1) 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
2) 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 다시 방문을 진행하면, 연결된 모든 지점을 방문할 수 있다. -> 얼음 보숭이 하나 제작
3) 1, 2번 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.

"""
# 내 풀이
n, m = map(int, input().split(' '))
shape = []
for _ in range(n):
    shape.append(list(map(int, input())))

# 책 풀이
n, m = map(int, input().split(' '))
graph = []
for i in range(n):
    graph.append(list(map(int, input())))           # 띄어쓰기 안 하고 입력했을 때 글자 하나를 원소로 받는 방법

def dfs(x, y):                                      # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    if x <= -1 or x >= n or y <= -1 or y >= m:      # x 또는 y가 얼음틀을 벗어나면 False로 return
        return False
    if graph[x][y] == 0:                            # 탐색하는 위치가 0이면...
        graph[x][y] = 1                             # 탐색하는 위치를 1로 바꾸고...
        dfs(x - 1, y)                               # 상, 좌, 하, 우 위치를 재귀적으로 함수 호출하여 탐색
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True                                 # 그리고 True로 return
    return False                                    # 탐색하는 위치가 0이 아니면 False로 return

result = 0                                          # 얼음보숭이 개수
for i in range(n):                                  # 전체 탐색하며 모든 노드에 음료수 채우기
    for j in range(m):
        if dfs(i, j) == True:                       # 현재 위치에서 DFS 수행
            result += 1

print(result)
