"""

[숫자 카드 게임]
: 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

핵심 : 각 행마다 가장 작은 수를 찾은 뒤에 그 중 가장 큰 수를 찾으면 됨
->

"""
# 내 풀이
n, m = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))

row_min = []
for i in range(n):
    row_min.append(min(data[i]))
ans = max(row_min)

print(ans)

# 책 - min() 함수를 이용하는 답안 예시
n, m = map(int, input().split(' '))

result = 0
for i in range(n):
    data = list(map(int, input().split(' ')))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 책 - 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split(' '))

result = 0
for i in range(n):
    data = list(map(int, input().split(' ')))
    min_value = 10001
    for i in data:
        min_value = min(min_value, i)
    result = max(result, min_value)

print(result)