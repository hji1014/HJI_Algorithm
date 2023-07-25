"""

문제 이름 : 부품 찾기(이진 탐색 이용)

핵심 : 이진 탐색

"""
import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split(' ')))

array.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')