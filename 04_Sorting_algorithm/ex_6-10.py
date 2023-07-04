"""

문제 이름 : 위에서 아래로

핵심 :

"""
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for i in sorted(array, reverse=True):
    print(i, end=' ')