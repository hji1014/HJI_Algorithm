# 두 수의 차
def solution(num1, num2):
    return num1 - num2

# 몫 구하기
def solution(num1, num2):
    return num1 // num2

# 나머지 구하기
def solution(num1, num2):
    return num1 % num2

# 두 수의 곱
def solution(num1, num2):
    return num1 * num2

# 숫자 비교하기
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

# 나이 출력
def solution(age):
    birth = 2023 - age
    return birth

# 두 수의 합
def solution(num1, num2):
    return num1 + num2

# 두 수의 나눗셈
def solution(num1, num2):
    return int(1000 * (num1 / num2))

# 각도기
def solution(angle):
    answer = 0
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90< angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    else:
        pass
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            answer += i
        else:
            pass
    return answer
