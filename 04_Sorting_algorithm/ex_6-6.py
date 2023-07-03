"""

문제 이름 : 계수 정렬 소스코드

핵심 : 각 데이터가 몇번 등장했는지 count하여 출력, 정수형 데이터 + 최대값과 최소값의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능

"""
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0 for _ in range(max(array) + 1)]

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')