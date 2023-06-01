"""

[1이 될 때까지]
: -1, /k(n이 k로 나누어 떨어질 때만) 두 가지 연산을 사용하여 n을 1로 만드는 최소 연산 횟수 구하기

핵심 : 최대한 나누기(/k)를 많이 해야함
->

"""

# 내 코드
"""
<틀린 이유>
: 맞나? 채점이 없어서 잘 모르겠다.
"""
n, k = map(int, input().split(' '))
count = 0

while n > 1:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# 책 - 단순하게 푸는 답안 예시 (시간 초과날 수 있음)
n, k = map(int, input().split(' '))
result = 0

while n >= k:           # n이 k 이상이라면 k로 계속 나누기
    while n % k != 0:   # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
        n -= 1
        result += 1
    n //= k             # k로 나누기
    result += 1

while n > 1:            # 마지막으로 남은 수에 대하여 1씩 빼기
    n -= 1
    result += 1

print(result)

# 책 - 효율적인 코드
n, k = map(int, input().split(' '))
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)