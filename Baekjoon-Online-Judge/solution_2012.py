"""
[등수 매기기]
"""
# 내 풀이 (1)
"""
틀린 이유 : 시간초과
"""
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

check = [False] * n
unsatisfied = 0

for i in range(len(data)):
    if check[data[i] - 1] == False:
        check[data[i] - 1] = True
    else:
        for j in range(len(check)):
            if check[j] == False:
                check[j] = True
                unsatisfied += abs(data[i] - (j + 1))
                break

print(unsatisfied)

# 내 풀이 (2)
"""
틀린 이유 : 로직이 틀림
"""
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

ideal = 0
for i in range(1, n + 1):
    ideal += i
real = sum(data)

print(abs(ideal - real))

# 블로그 풀이 (1)
"""
ref : https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-2012.-%EB%93%B1%EC%88%98%EB%A7%A4%EA%B8%B0%EA%B8%B0-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-2
틀린 이유 : 시간 초과 - PyPy3로만 통과
"""
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

result = 0
for i in range(1, n + 1):
    result += abs(i - data[i - 1])

print(result)

# 블로그 풀이 (2)
"""
맞은 이유 : 입력 데이터가 많을 땐 sys.stdin.readline().rstrip()으로 입력 받는 것이 시간복잡도 측면에서 유리함
"""
import sys
n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort()
result = 0
for i in range(1, n + 1):
    result += abs(i - data[i - 1])

print(result)
