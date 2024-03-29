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

# 배열 두배 만들기
def solution(numbers):
    return [i * 2 for i in numbers]

# 정수 부분
def solution(flo):
    return int(flo)

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0

# 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)

# 공배수
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit() == True:
            answer += int(i)
    return answer

# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(n + 1):
        if i % 2 != 0:
            answer.append(i)
    return answer

# 문자열안에 문자열
def solution(str1, str2):
    if str2 in str1:
        return 1
    return 2

# 대문자로 바꾸기
def solution(myString):
    answer = ''
    for i in myString:
        answer += i.upper()
    return answer

# n의 배수
def solution(num, n):
    if num % n == 0:
        return 1
    return 0

# 문자열 정수의 합
def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer

# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1 + str2)

# 수 조작하기 1
def solution(n, control):
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10
    return  n

# n개 간격의 원소들
def solution(num_list, n):
    answer = []
    order = 0
    while True:
        answer.append(num_list[n * order])
        order += 1
        if (n * order) > len(num_list) - 1:
            break
    return answer

# 소문자로 바꾸기
def solution(myString):
    answer = ''
    for i in myString:
        answer += i.lower()
    return answer

# 문자열의 앞에 n글자
def solution(my_string, n):
    return my_string[0:n]

# 조건에 맞게 수열 변환하기
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i / 2)
        elif i < 50 and i % 2 == 1:
            answer.append(i * 2)
        else:
            answer.append(i)
    return answer

# 길이에 따른 연산
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        answer = 1
        for i in num_list:
            answer *= i
        return answer

# 카운트 업
def solution(start, end):
    answer = []
    for i in range(start, end + 1):
        answer.append(i)
    return answer

# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b

# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp:
            answer += i.upper()
        else:
            answer += i
    return answer

# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# n 번째 원소부터
def solution(num_list, n):
    return num_list[(n -1):]

# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer

# 문자열로 변환
def solution(n):
    return str(n)

# 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(2 * num_list[-1])
    return num_list

# 문자열 곱하기
def solution(my_string, k):
    return my_string * k

# 카운트 다운
def solution(start, end):
    return [i for i in range(start, end - 1, -1)]

# 첫 번째로 나오는 음수
def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    if answer == 0:
        return -1
