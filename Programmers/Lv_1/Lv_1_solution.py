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

# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))

for _ in range(b):
    print("*" * a)

# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    n_factor = []
    m_factor = []
    GCD = []
    LCM = []

    # n, m 약수 구하기
    for i in range(1, n + 1):  # n 약수
        if n % i == 0:
            n_factor.append(i)
        else:
            pass

    for j in range(1, m + 1):  # m 약수
        if m % j == 0:
            m_factor.append(j)
        else:
            pass

    # 최대공약수 구하기
    for i in n_factor:
        if i in m_factor:
            GCD.append(i)
        else:
            pass
    answer.append(max(GCD))

    # 최소공배수 구하기
    for i in range(1, (n * m) + 1):
        if i % n == 0 and i % m == 0:
            LCM.append(i)
    answer.append(min(LCM))

    return answer

# 같은 숫자는 싫어
def solution(arr):
    answer = []
    next_index = 0
    arr.append(11)          # 들어올 수 있는 수는 0~9 사이의 정수. 입력 마지막에 '11'을 넣어주는 것이 관건이었음

    for i in arr:
        next_index += 1
        if next_index >= len(arr):
            break
        if i != arr[next_index]:
            answer.append(i)

    return answer

# 3진법 뒤집기 (내 풀이 - 틀렸음)
"""
<틀린 이유>
: 몫이 3보다 작을 때 1을 넣는 것이 아니고... 2가 나올 수도 있음
"""
def solution(n):
    arr = []
    m = 0
    answer = 0

    # 3진수로 변환
    while True:
        if n >= 3:
            share = n // 3
            reminder = n % 3
            n = share
            m = reminder
            arr.append(m)  # 원래 3진법 결과가 앞뒤 반전되어서 나옴
            #if share < 3:
            #    arr.append(1)       # 이게 틀림 -> 2가 나올 수 있음
            #    break
        else:
            arr.append(n)
            #answer = n
            break

    arr.reverse()  # 앞뒤 반전을 해야 10진법으로 바꾸기 편함
    print(arr)

    # 10진법으로 표현
    import math     # 함수 앞에 하기
    for i in range(len(arr)):
        answer += arr[i] * math.pow(3, i)

    return int(answer)

# 3진법 뒤집기 (블로그 풀이)
def solution(n):

    answer = ''

    while n >= 1:
        rest = n % 3
        n = n // 3
        answer += str(rest)
    print(answer)

    return int(answer, 3)

# 이상한 문자 만들기 (내 풀이 - 틀렸음)
"""
<틀린 이유>
: 아마 중간 if문이 틀린듯. 마지막 공백 문제를 해결할려면 return할 때 인덱싱을 [0:-1]로 하면 됨.
"""
def solution(s):
    answer = ''
    sp = s.split(' ')       # 띄어쓰기를 기준으로 나눈다는 뜻

    for voca in sp:
        for i in range(len(voca)):
            if i % 2 == 0:            # 이 조건은 if i % 2 == 0:과 같음
                answer += voca[i].upper()
            elif i % 2 == 1:          # 이 조건은 if i % 2 == 1:과 같음
                answer += voca[i].lower()
        if voca == sp[len(sp) - 1]:         # 이 놈이 문제였음 -> 케이스 여러 개 틀리면 로직이 틀림
            break                           # 공백이 여러 개 있어서 문제가 생긴 듯
        answer += ' '

    return answer

# 이상한 문자 만들기 (블로그 풀이)
def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]

# 예산
def solution(d, budget):

    answer = 0
    cost_sum = 0
    d.sort()                        # 여기서 핵심은 budget을 완벽히 소진할 필요는 없다는 것
    for i in d:
        cost_sum += i
        if cost_sum > budget:       # 같을 때도 answer에 +1을 해줘야 함
            break
        answer += 1

    return answer

# 삼총사
def solution(number):
    answer = 0
    import itertools
    for i in itertools.combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer

# 시저 암호
def solution(s, n):
    answer = ''
    #print(ord('A'), ord('Z'), ord('a'), ord('z'))
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif s[i].isupper():
            num = (ord(s[i]) - 65 + n) % 26     # 0과 25 사이로 만들어 놓고 shifting을 시켜준 이후에 26으로 나눈 나머지 값은 어짜피 0~25 사이로 나옴. 이게 핵심
            answer += chr(num + 65)
        elif s[i].islower():
            num = (ord(s[i]) - 97 + n) % 26
            answer += chr(num + 97)
        else:
            pass
    return answer

# 시저 암호 (join() 함수 썼을 때)
def solution(s, n):         # join() 쓰면 조건을 줄여줄 수 있음
    answer = ''
    s = list(s)
    # print(ord('A'), ord('Z'), ord('a'), ord('z'))
    for i in range(len(s)):
        if s[i].isupper():
            num = (ord(s[i]) - 65 + n) % 26
            s[i] = chr(num + 65)
        elif s[i].islower():
            num = (ord(s[i]) - 97 + n) % 26
            s[i] = chr(num + 97)

    return "".join(s)

# 최소 직사각형
def solution(sizes):
    w_w = []
    w_h = []

    for i in sizes:
        w_w.append(max(i))
        w_h.append(min(i))
    answer = max(w_w) * max(w_h)

    return answer

# 크기가 작은 부분 문자열
def solution(t, p):
    count = 0

    for i in range(len(t) - len(p) + 1):  # range 값 핵심
        temp = int(t[i:i + len(p)])
        if temp <= int(p):
            count += 1

    return count

# [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    answer_encoding = []
    arr1_decoding = []
    arr2_decoding = []

    for i in range(n):
        remainders = []
        num = arr1[i]
        while num != 0:
            remainder = num % 2
            remainders.append(remainder)
            num = num // 2
        while len(remainders) != n:
            remainders.append(0)
        remainders.reverse()
        arr1_decoding.append(remainders)

    for i in range(n):
        remainders = []
        num = arr2[i]
        while num != 0:
            remainder = num % 2
            remainders.append(remainder)
            num = num // 2
        while len(remainders) != n:
            remainders.append(0)
        remainders.reverse()
        arr2_decoding.append(remainders)

    for i in range(n):
        answer_row = []
        for j in range(n):
            arr1_row = arr1_decoding[i]
            arr2_row = arr2_decoding[i]
            if arr1_row[j] == 0 and arr2_row[j] == 0:
                answer_row.append(0)
            else:
                answer_row.append(1)
        answer_encoding.append(answer_row)

    for i in range(n):
        ans = ''
        for j in range(n):
            if answer_encoding[i][j] == 1:
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)

    return answer

# [1차] 비밀지도 (다른 사람의 간략한 풀이)
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1','#')
        a12 = a12.replace('0',' ')
        answer.append(a12)
    return answer

# 숫자 문자열과 영단어
def solution(s):
    num_dict = dict()
    num_dict['zero'] = '0'
    num_dict['one'] = '1'
    num_dict['two'] = '2'
    num_dict['three'] = '3'
    num_dict['four'] = '4'
    num_dict['five'] = '5'
    num_dict['six'] = '6'
    num_dict['seven'] = '7'
    num_dict['eight'] = '8'
    num_dict['nine'] = '9'
    key_list = num_dict.keys()

    for i in key_list:
        if i in s:
            print(type(i))
            s = s.replace(i, num_dict[i])

    answer = int(s)

    return answer

# 문자열 내 마음대로 정렬하기 (내 풀이)
"""
<틀린 이유>
: 간단하지만 기발한 아이디어를 생각해내야 함. 아니면 너무 어려운 로직을 구현해야함. 그러면 시간이 많이 걸리고, 구현이 불가능하기도 함.
"""
def solution(strings, n):
    answer = []
    rank = []
    rank_index = []
    target_others = []

    for i in strings:
        # others = i[n:].split(' ')와 다름
        others = list(i[n + 1:])
        others_sum = 0
        for j in others:
            others_sum += ord(j)

        list_2d = [ord(i[n]), others_sum]
        # [n번째 유니코드, n+1번째 이후 유니코드의 합]
        target_others.append(list_2d)
        # rank.append(ord(i[n]))
    rank_sorted = sorted(rank)
    print(rank_sorted)

    for i in range(len(rank_sorted)):
        print(i)
    for i in rank_sorted:
        rank_index.append(rank.index(i))

    # 똑같은 경우 뒤에 문자 번호 다 더해서 작은 순으로
    # for i in
    # print(rank_index)

    for i in rank_index:
        answer.append(strings[i])

    return answer

# 문자열 내 마음대로 정렬하기 (블로그 풀이)
def solution(strings, n):
    temp = []
    answer = []

    for i in strings:
        temp.append(i[n] + i)       # target 알파벳을 각각의 단어 앞에 합쳐줌
    temp.sort()                     # temp를 정렬 시킨 후
    for j in temp:
        answer.append(j[1:])        # 맨 앞 target 알파벳 뒤부터 떼어서 제출

    return answer

# K번째수
def solution(array, commands):
    answer = []
    for i in commands:
        temp_arr = array[(i[0]-1):i[1]]
        temp_arr.sort()
        temp_element = temp_arr[i[2]-1]
        answer.append(temp_element)
    return answer

# 두 개 뽑아서 더하기
import itertools

def solution(numbers):
    sums = []

    for i in itertools.combinations(numbers, 2):
        sums.append(sum(i))
    sums_set = set(sums)        # 중복제거 방법 : 리스트에서 셋으로 바꿨다가 다시 리스트로 변환
    answer = list(sums_set)
    answer.sort()

    return answer

# 푸드 파이트 대회
def solution(food):
    answer = ''
    food_num = 1
    arr1 = []

    for i in food[1:]:
        if i % 2 == 1:
            i -= 1
        for j in range(i // 2):
            arr1.append(food_num)
        food_num += 1

    arr2 = arr1.copy()
    arr2.reverse()          # reverse() 함수를 사용하면 원본 리스트가 변환되므로 copy()로 복사하고 해야 함
    answer_list = arr1 + [0] + arr2

    for i in answer_list:
        answer += str(i)

    return answer

# 콜라 문제 (내 풀이)
"""
<틀린 이유>
: 빈 병의 현재 상태는 n=n//a가 아니라 n=b*(n//a)라는 개념을 틀린듯 함.
"""
def solution(a, b, n):
    a = 3
    b = 1
    n = 20
    answer = 0
    remainder = 0
    while n > 0:
        answer += b * (n // a)
        remainder += n % a              # 이걸 n에 더해야 함
        if remainder >= a:
            answer += b * (remainder // a)
            remainder -= remainder // a
        n = n // a  # 여기가 틀린듯. n의 현재 상태는 (n//a) * b로 되어야지...
    print(answer)

    return answer

# 콜라 문제 (블로그 풀이)
"""
ref : https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%BD%9C%EB%9D%BC-%EB%AC%B8%EC%A0%9C-Python
"""
def solution(a, b, n):
    answer = 0
    # 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
    # 빈 병의 개수가 콜라를 받기 위해서 필요한 개수보다 크면 반복한다
    while n >= a:
        remain_bottle = n % a
        n = (n//a) * b # 마트에서 받은 콜라의 수
        answer += n # 받은 걸 answer에 +
        n += remain_bottle # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    return answer

# 가장 가까운 같은 글자
def solution(s):
    answer = []
    s_list = list(s)
    for i in range(len(s_list)):
        if i == 0:
            answer.append(-1)
        else:
            if s_list[i] in s_list[:i]:
                temp_reverse = s_list[:i].copy()
                temp_reverse.reverse()
                temp_index = temp_reverse.index(s_list[i])
                answer.append(temp_index + 1)
            else:
                answer.append(-1)
    return answer

# 추억 점수
def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    for i, j in zip(name, yearning):
        score_dict[i] = j
    for i in range(len(photo)):
        answer_score = 0
        intersection = set(name) & set(photo[i])    # 교집합 찾기
        intersection = list(intersection)
        for j in intersection:
            answer_score += score_dict[j]
        answer.append(answer_score)
    return answer

# 2016년
def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    last_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = [i for i in range(1, 13)]
    calendar = {}  # "3월5일" : 'SAT'
    count = 0
    for i in month:
        for j in range(1, last_date[i - 1] + 1):
            order = count % 7
            name = f'{i}_{j}'
            calendar[name] = day[order]
            count += 1
    answer_date = f'{a}_{b}'
    answer = calendar[answer_date]

    return answer

# 폰켓몬
def solution(nums):
    answer = 0
    set_nums = set(nums)
    if len(nums) // 2 < len(set_nums):
        answer = len(nums) // 2
    else:
        answer = len(set_nums)
    return answer

# 명예의 전당 (1)
def solution(k, score):
    answer = []
    k_arr = []
    for i in range(len(score)):
        if i < k:
            k_arr.append(score[i])
            answer.append(min(k_arr))
        else:
            k_arr.append(score[i])
            k_arr.remove(min(k_arr))
            answer.append(min(k_arr))
    return answer

# 모의고사
def solution(answers):
    answer = []
    score_1 = 0
    score_2 = 0
    score_3 = 0
    answer_1 = []
    answer_2 = []
    answer_3 = []
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    share_1 = len(answers) // len(pattern_1)
    remainder_1 = len(answers) % len(pattern_1)
    answer_1 = answer_1 + (pattern_1 * share_1) + pattern_1[0:remainder_1]

    share_2 = len(answers) // len(pattern_2)
    remainder_2 = len(answers) % len(pattern_2)
    answer_2 = answer_2 + (pattern_2 * share_2) + pattern_2[0:remainder_2]

    share_3 = len(answers) // len(pattern_3)
    remainder_3 = len(answers) % len(pattern_3)
    answer_3 = answer_3 + (pattern_3 * share_3) + pattern_3[0:remainder_3]

    for i, j, k, l in zip(answers, answer_1, answer_2, answer_3):
        if j == i:
            score_1 += 1
        else:
            pass
        if k == i:
            score_2 += 1
        else:
            pass
        if l == i:
            score_3 += 1
        else:
            pass

    scores = [score_1, score_2, score_3]
    max_scores = max(scores)
    for i in range(3):
        if scores[i] == max_scores:
            answer.append(i + 1)

    return answer

# 과일 장수
def solution(k, m, score):
    answer = 0
    box_num = len(score) // m
    all_package = []

    if box_num == 0:
        return 0
    else:
        score_sort = sorted(score, reverse=True)
        for i in range(box_num):
            package = []
            for j in range(m):
                package.append(score_sort[j + (i * m)])
            all_package.append(package)
        for i in all_package:
            answer += min(i) * m
        return answer

# 소수 만들기

# 소수 찾기 (내 풀이)
"""
틀린 이유 : 시간 초과
"""
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        judge = 0
        if i == 1:
            pass
        else:
            for j in range(1, i + 1):
                if i % j == 0:
                    judge += 1
                else:
                    pass
            if judge <= 2:
                answer += 1
            else:
                pass
    return answer

# 소수 찾기 (블로그 풀이)
"""
에라토스테네스의 체(Sieve of Eratosthenes) 방법 사용된 코드
ref : https://wackylife.tistory.com/22
"""
def solution(n):
    answer = 0
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))  # i가 num 안에 있으면, i를 제외한 i의 배수를 모두 제거
    answer = len(num)
    return answer

#
