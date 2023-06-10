"""
[미로 탐색]
"""
# 시작 -> (1, 1) 무조건 1 -> 1 옆에 1 있으면 하나 추가해서 변환
n, m = map(int, input().split(' '))
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

#f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2178.txt', 'r')
#n, m = map(int, f.readline().rstrip().split(' '))
#graph = []
#for _ in range(n):
#    graph.append(list(map(int, f.readline().rstrip())))
#f.close()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = [(0, 0)]

def bfs():
    while q:
        x, y = q[0][0], q[0][1]
        del q[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
        #print("무한반복")

bfs()

print(graph[n - 1][m - 1])