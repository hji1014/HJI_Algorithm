"""

문제 이름 : 부품 찾기(집합 자료형 이용)

핵심 : 계수 정렬

"""
import sys
n = int(sys.stdin.readline().rstrip())
array = set(map(int, sys.stdin.readline().rstrip().split(' ')))
m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')