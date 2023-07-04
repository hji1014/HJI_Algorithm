"""

문제 이름 : 성적이 낮은 순서로 학생 출력하기

핵심 :

"""
n = int(input())
array = []
for _ in range(n):
    a, b = input().split(' ')
    array.append((a, int(b)))

score_sorted = sorted(array, key=lambda x : x[1])

for c, d in score_sorted:
    print(c, end=' ')