"""
[네트워크 연결]
ref : https://velog.io/@slbin-park/%EB%B0%B1%EC%A4%80-1922%EB%B2%88-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%97%B0%EA%B2%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
최소스패닝 트리 구현

"""
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1922.txt', 'r')
#n = int(input())
n = int(f.readline().rstrip())
#m = int(input())
m = int(f.readline().rstrip())
costs = []
for _ in range(m):
    #a, b, c = map(int, input().split(' '))
    a, b, c = map(int, f.readline().rstrip().split(' '))
    costs.append((c, a, b))
f.close()

costs.sort(key=lambda x : x[0])
parent = [i for i in range(n + 1)]
cost = 0

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

for dis, a, b in costs:
    if find(a) != find(b):
        union(a, b)
        cost += dis

print(cost)