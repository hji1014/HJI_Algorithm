"""

[APPENDIX A - 코딩 테스트를 위한 파이썬 문법]

[2] 조건문
: 조건문은 프로그램을 작성할 때 프로그램의 흐름을 제어하는 문법이다. 조건문을 이용하면 조건에 따라서 프로그램의 로직을 설정할 수 있다.

1-1) 예제

1-2) 비교 연산자

1-3) 논리 연산자

1-4) 파이썬의 기타 연산자

"""

# x가 10 이상일 때만 x를 출력
x = 15
if x >= 10:
    print(x)

# 성적 구간에 따른 학점 정보 출력
"""
(조건)
i) 성적이 90점 이상일 때 : A
ii) 성적이 90점 미만, 80점 이상일 때 : B
iii) 성적이 80점 미만, 70점 이상일 때 : C
iv) 성적이 70점 미만일 때 : F
"""
def score_result(score):            # 내가 짠 코드

    if score >= 90:
        print('학점 : A')
    elif score >= 80 and score < 90:
        print('학점 : B')
    elif score >= 70 and score < 80:
        print('학점 : C')
    else:
        print('학점 : F')

score = 85
score_result(score)

# 책에 나온 더 효율적인 코드
score = 85

if score >= 90:
    print('학점 : A')
elif score >= 80:
    print('학점 : B')
elif score >= 70:
    print('학점 : C')
else:
    print('학점 : F')

### 비교 연산자 ###
x = 10
y = 20

print(x == y)   # x와 y가 같으면 True
print(x != y)   # x와 y가 다르면 True
print(x > y)    # x가 y보다 크면 True
print(x < y)    # x가 y보다 작으면 True
print(x >= y)   # x가 y보다 같거나 크면 True
print(x <= y)   # x가 y보다 같거나 작으면 True

### 논리 연산자 ###
x = 10
y = 20

print(x != y and x <= y)        # a and b : a와 b가 모두 True일 때 True
print(x != y and x > y)         # a or b : a 또는 b 중에 하나라도 True일 때 True
print(not x == y)               # not a : a가 거짓일 때 True

### 파이썬의 기타 연산자 ###
m = [1, 2, 3, 4]
print(1 in m)       # a in 리스트/문자열/튜플/사전 : a가 리스트/문자열/튜플/사전 안에 있으면 True
print(1 not in m)   # a not in 리스트/문자열/튜플/사전 : a가 리스트/문자열/튜플/사전 안에 없으면 True

# pass 문 -> 조건이 True여도 아무것도 처리하고 싶지 않을 때
score = 85

if score >= 80:
    pass    # 나중에 작성할 코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 간략하게 표현하기 -> 조건문에서 실행될 소스코드가 한 줄인 경우
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

print(result)

# 조건부 표현식(conditional expression) 사용하여 더 간단히 표현
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# 조건부 표현식 사용하여 리스트에 있는 원소 값 변경/제거 (method 1)
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# 조건부 표현식 사용하여 리스트에 있는 원소 값 변경/제거 (method 1)
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)

# 파이썬 조건문 내에서의 부등식

x = 15
if x > 0 and x < 20:                        # method 1
    print("x는 0 초과 20 미만의 수입니다.")

if 0 < x < 20:                              # method 2
    print("x는 0 초과 20 미만의 수입니다.")



















