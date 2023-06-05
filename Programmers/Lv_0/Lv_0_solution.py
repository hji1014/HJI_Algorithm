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

# 배열의 평균값
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    answer /= len(numbers)
    return answer

# 양꼬치
def solution(n, k):
    if n >= 10:
        k -= n // 10
    return n * 12000 + k * 2000

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 아이스 아메리카노
def solution(money):
    return [money // 5500, money % 5500]

# 편지
def solution(message):
    return len(message) * 2

# 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4

# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 삼각형의 완성조건 (1)
def solution(sides):
    sides.sort(reverse=True)
    if sides[0] < sides[1] + sides[2]:
        return 1
    else:
        return 2

# 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array)//2]

# 최댓값 만들기 (1)
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]
