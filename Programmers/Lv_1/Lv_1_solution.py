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

# 하샤드 수
def solution(x):
    x_str = str(x)
    x_len = len(x_str)

    sum = 0

    for i in range(x_len):
        sum += int(x_str[i])

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer

# 두 정수 사이의 합
def solution(a, b):
    answer = 0

    if a > b:
        for i in range(b, a + 1):
            answer += i
    elif a < b:
        for i in range(a, b + 1):
            answer += i
    elif a == b:
        answer = a

    return answer

# 콜라츠 추측
def solution(num):
    answer = 0
    state = True
    while state == True:
        if num == 1:
            answer = 0
            state = False
        else:
            if num % 2 == 0:
                num = num / 2
                answer += 1
                if num == 1:
                    state = False
                elif answer >= 500:
                    answer = -1
                    state = False
            elif num % 2 == 1:
                num = (num * 3) + 1
                answer += 1
                if num == 1:
                    state = False
                elif answer >= 500:
                    answer = -1
                    state = False

    return answer

# 서울에서 김서방 찾기
def solution(seoul):
    seoul_len = len(seoul)
    for i in range(seoul_len):
        if seoul[i] == 'Kim':
            answer = f'김서방은 {i}에 있다'
        else:
            pass

    return answer

# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        else:
            pass

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()           # a = a.sort()가 안됨 주의 !!!

    return answer

# 핸드폰 번호 가리기
def solution(phone_number):
    number_len = len(phone_number)
    star = '*' * (number_len - 4)
    real_num = phone_number[(number_len - 4):number_len]
    answer = star + real_num
    return answer

# 음양 더하기 (method 1)
def solution(absolutes, signs):

    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * -1

    return answer

#  음양 더하기  (method 2 - zip() 함수 적용)
def solution(absolutes, signs):
    answer = 0

    for absol, sig in zip(absolutes, signs):
        if sig:
            answer += absol
        else:
            answer -= absol

    return answer

# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(10):
        if i in numbers:
            pass
        else:
            answer += i

    return answer

# 제일 작은 수 제거하기
def solution(arr):
    answer = []
    min_comp = min(arr)

    if len(arr) != 1:
        arr.remove(min_comp)
        answer = arr
    else:
        answer.append(-1)

    return answer

# 가운데 글자 가져오기
def solution(s):
    s_len = len(s)

    if s_len % 2 == 1:
        answer = s[int(s_len // 2)]
    else:
        if s_len == 2:
            answer = s
        else:
            answer = s[int(s_len // 2) - 1:int(s_len // 2) + 1]

    return answer

# 수박수박수박수박수박수?
def solution(n):
    if n == 1:
        answer = '수'
    else:
        if n % 2 == 0:
            answer = '수박' * int(n / 2)
        else:
            answer = '수박' * int(n / 2) + '수'

    return answer

# 내적
def solution(a, b):
    answer = 0

    for a_i, b_i in zip(a, b):
        answer += a_i * b_i

    return answer

# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''
    sorted_s = sorted(s, reverse=True)

    for i in sorted_s:
        answer += i

    return answer

# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        num_list = []
        for j in range(1, i + 1):
            if i % j == 0:
                num = i / j
                num_list.append(num)
                num_len = len(num_list)
            else:
                pass
        if num_len % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

# 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    all_price = 0

    for i in range(count):
        all_price += price * (i + 1)

    need_price = money - all_price

    if need_price >= 0:
        answer = 0
    else:
        answer = abs(need_price)

    return answer

# 문자열 다루기 기본
def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:         # isdigit(), isalpha() 함수 모르면 풀기 힘듦
            answer = True
        else:
            answer = False
    else:
        answer = False

    return answer

# 행렬의 덧셈 -> arr1 = [[1, 2], [2, 3]] -> z = arr1[0][1] 이건 왜 안되지?
def solution(arr1, arr2):
    mat_size = len(arr1)
    answer = [[0] * mat_size for _ in range(mat_size)]

    for i in range(mat_size):
        empty_mat = []
        arr1_row = arr1[i]
        arr2_row = arr2[i]
        for arr1_comp, arr2_comp in zip(arr1_row, arr2_row):
            comp_sum = arr1_comp + arr2_comp
            empty_mat.append(comp_sum)
        answer[i] = empty_mat

    return answer

