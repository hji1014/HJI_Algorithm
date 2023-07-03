"""

문제 이름 : 퀵 정렬 소스코드

핵심 : 가장 직관적인 형태의 퀵 정렬 소스코드

"""
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:        # 원소가 1개인 경우 종료
        return
    pivot = start           # 피벗은 첫 번째 원소
    left = start + 1        # left는 왼쪽부터 탐색하는 원소의 인덱스
    right = end             # right는 오른쪽부터 탐색하는 원소의 인덱스
    while left <= right:    # left가 right보다 작거나 같은 한 계속 반복
        while left <= end and array[left] <= array[pivot]:              # 피벗보다 큰 데이터를 찾을 때까지 반복
            left += 1
        while right > start and array[right] >= array[pivot]:           # 피벗보다 작은 데이터를 찾을 때까지 반복
            right -= 1
        if left > right:                                                # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:                                                           # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)         # 분할 이후 왼쪽 부분에서 정렬 수행
    quick_sort(array, right + 1, end)           # 분할 이후 오른쪽 부분에서 정렬 수행

quick_sort(array, 0, len(array) - 1)
print(array)
