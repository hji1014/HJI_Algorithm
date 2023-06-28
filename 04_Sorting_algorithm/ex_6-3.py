"""

문제 이름 : 삽입 정렬 소스코드

핵심 : 이미 거의 정렬되어 있는 데이터일 때 가장 효과적!

"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):                                   # 왼쪽으로 한 칸씩 계속 옮기기(작다면)
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]     # 스와프
        else:
            break

print(array)