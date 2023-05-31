"""
문제 이름 : 큰 수의 법칙

핵심 : 가장 큰 수와 두 번째로 큰 수만 저장하면 됨
->

"""
# 단순하게 푸는 답안 (m이 100억 이상이면 시간 초과)
n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
data.sort(reverse=True)
first = data[0]
second = data[1]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break       # break는 반복문 단 하나만 빠져나올 수 있음
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 모범 답안
n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
data.sort(reverse=True)
first = data[0]
second = data[1]

# 가장 큰 수가 더해지는 횟수 계산
count = (m // (k + 1)) * k      # m 나누기 k+1 덩어리가 반복되는 수의 몫에 k를 곱한 수 : m이 k+1로 나누어 떨어질 때 가장 큰 수가 반복되는 수
count += m % (k + 1)            # m이 k+1로 나누어떨어지지 않는 경우 고려

result = 0
result += (count) * first
result += (m - count) * second  # 두 번째로 큰 수가 더해지는 횟수 = (m - count)

print(result)