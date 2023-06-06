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

# 피자 나눠 먹기(3)
def solution(slice, n):
    answer = 1
    while True:
        if slice * answer - n >= 0:
            break
        else:
            answer += 1
    return answer

# 문자열 뒤집기
def solution(my_string):
    answer = ''
    str_list = list(my_string)
    str_list.reverse()
    for i in str_list:
        answer += i
    return answer

# 편지
def solution(message):
    return len(message) * 2

# 피자 나눠 먹기 (1)
def solution(n):
    answer = 1
    while True:
        if 7 * answer / n >= 1:
            break
        else:
            answer += 1
    return answer

# 짝수 홀수 개수
def solution(num_list):
    even_num = 0
    odd_num = 0
    for i in num_list:
        if i % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    return [even_num, odd_num]

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

# 옷가게 할인 받기
def solution(price):
    if price < 100000:
        return price
    elif 100000 <= price < 300000:
        return int(price * 0.95)
    elif 300000 <= price < 500000:
        return int(price * 0.9)
    elif price >= 500000:
        return int(price * 0.8)

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

# 중복된 숫자 개수
def solution(array, n):
    return array.count(n)

# 특정 문자 제거하기
def solution(my_string, letter):
    str_list = list(my_string)
    for i in str_list.copy():
        if i == letter:
            str_list.remove(i)
    return ''.join(str_list)

# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
    return num_list

# 배열의 유사도
def solution(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    return len(s1_set & s2_set)

# 순서쌍의 개수
import itertools
def solution(n):
    answer = 0
    cm = []
    for i in range(1, n + 1):
        if n % i == 0:
            cm.append(i)
    return len(cm)

# 모음 제거
def solution(my_string):
    l = list(my_string)
    m = set(['a', 'e', 'i', 'o', 'u'])
    for i in l.copy():
        if i in m:
            l.remove(i)
    answer = ''
    for i in l:
        answer += i
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer
