# 짝수와 홀수
def solution(num):
    if num % 2 == 1:
        answer = "Odd"
    else:
        answer = "Even"
    return answer

# 평균 구하기
def solution(arr):
    answer = 0

    sum_val = sum(arr)
    length_arr = len(arr)

    answer = sum_val / length_arr

    return answer

# 약수의 합
def solution(n):
    answer = 0

    for i in range(1, n + 1):
        a = n % i
        if a == 0:
            answer += i

    return answer

# 자릿수 더하기 --> 다시보기
def solution(n):
    answer = 0

    while n != 0:
        answer += n % 10
        n //= 10

    return answer

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    a = 0
    for i in range(1, n + 1):           # 그냥 range(n)으로 가능
        a += x
        answer.append(a)

    return answer

# 나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(1, n):
        a = n % i
        if a == 1:
            return i

# 문자열 내 p와 y의 개수
def solution(s):
    answer = True
    ss = s.upper()      # upper 대문자로, lower 소문자로
    cnt1, cnt2 = ss.count('P'), ss.count('Y')   # count 인자의 개수
    if cnt1 == cnt2:
        return True
    return False

# 자연수 뒤집어 배열로 만들기 (method 1)
def solution(n):
    m = list(map(int, str(n)))
    m.reverse()

    return m

# 자연수 뒤집어 배열로 만들기 (method 2)
def solution(n):
    m = list(map(int, str(n)))
    return list(reversed(m))

# 정수 제곱근 판별 (method 1)
import math

def solution(n):
    answer = 0
    a = math.sqrt(n)
    b = a % 1
    if b == 0:
        answer = (a + 1) * (a + 1)
    else:
        answer = -1

    return answer

# 정수 제곱근 판별 (method 2)
def solution(n):
    import math  # 함수 내부에 들어가도 됨
    answer = 0
    a = math.sqrt(n)
    b = a % 1
    if b == 0:
        answer = math.pow(a + 1, 2)
    else:
        answer = -1

    return answer

# 정수 제곱근 판별 (method 3)
def solution(n):
    import math  # 함수 내부에 들어가도 됨
    answer = 0
    a = math.sqrt(n)
    if a == int(a):
        answer = math.pow(a + 1, 2)
    else:
        answer = -1

    return answer

# 문자열을 정수로 바꾸기
def solution(s):
    answer = 0

    answer = int(s)
    return answer

# 정수내림차순으로 배치하기 (method 1)
def solution(n):
    answer = 0
    m = list(map(int, str(n)))
    m.sort()
    multi = 1

    for i in m:
        answer += i * multi
        multi *= 10

    return answer

# 정수내림차순으로 배치하기 (method 2)
def solution(n):
    answer = 0
    m = list(map(int, str(n)))
    a = list(sorted(m))
    print(a)
    multi = 1

    for i in a:
        answer += i * multi
        multi *= 10

    return answer












