"""

[APPENDIX A - 코딩 테스트를 위한 파이썬 문법]

[1] 자료형
: 파이썬의 자료형은 C/C++, 자바와 같은 다른 언어에서 사용되는 기본 자료형을 제공할 뿐만 아니라, 사전 자료형, 집합 자료형 등 강력한 기능을 제공하는 자료형을 기본으로 내장하고 있어 매우 편리하다.

1-1) 수 자료형(Number)
- 정수형(Integer)
- 실수형(Real Number)
- 수 자료형의 연산

1-2) 리스트 자료형
- 리스트 만들기
- 리스트의 인덱싱과 슬라이싱
- 리스트 컴프리헨션
- 리스트 관련 기타 메서드

1-3) 문자열 자료형
- 문자열 초기화
- 문자열 연산

1-4) 튜플 자료형

1-5) 사전 자료형
- 사전 자료형 소개
- 사전 자료형 관련 함수

1-6) 집합 자료형
- 집합 자료형 소개
- 집합 자료형의 연산
- 집합 자료형 관련 함수

"""

### 정수형 ###
a = 1000    # 양의 정수
print(a)

a = -7      # 음의 정수
print(a)

a = 0       # 0 (zero)
print(a)

### 실수형 ###
a = 156.93  # 양의 실수
print(a)

a = -1837.2 # 음의 실수
print(a)

a = 5.
print(a)    # 소수부가 0일 때 0을 생략

a = -.7     # 정수부가 0일 때 0을 생략
print(a)

a = 1e9     # 10억의 지수 표현 방식
print(a)

a = 75.25e1 # 752.5
print(a)

a = 3954e-3 #3.954
print(a)

# 2진수 체계의 한계점 - 미세한 오차 발생
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# 한계점 해결을 위한 round() 함수
a = 0.3 + 0.6
print(round(a, 4))          # a를 소수점 셋째(4-1=3) 자리에서 반올림, 두 번째 인자 안 쓰면 정수로 반올림

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

b = 3.73
b_round = round(b)

# 수 자료형의 연산
a = 7
b = 3

print(a * b)        # 곱하기
print(a / b)        # 나누기 -> 주의! : 기본적으로 실수형으로 처리
print(a % b)        # 나머지
print(a // b)       # 몫
print(a ** b)       # 거듭제곱

### 리스트 ###
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # 리스트 만들기
print(a)

print(a[4])                         # 인덱스 4, 즉 다섯 번째 원소에 접근(인덱스 순서 0->1->2->...)

a = list()                          # 빈 리스트 선언 방법 (1)
print(a)

a = []                              # 빈 리스트 선언 방법 (2)
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[-1])                        # 뒤에서 첫 번째 원소 출력
print(a[-3])                        # 뒤에서 세 번째 원소 출력

a[3] = 7                            # 네 번째 원소 값 변경
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])                       # 두 번째 원소부터 네 번째 원소까지 출력

# 리스트 컴프리헨션 : 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있음
array = [i for i in range(20) if i % 2 == 1]        # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
print(array)

# 위의 코드를 정석으로 작성하면 아래와 같음
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
        # array[i] = i 이렇게 하면 안됨... 빈 리스트라서
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i ** i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
array[1][2] = 5
print(array)

# 언더바(_) 역할
summary = 0                     # 언더바 없는 경우 : 반복을 위한 변수의 값이 필요한 경우
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(5):              # 언더바 있는 경우 : 반복을 위한 변수의 값이 필요하지 않고 단순 반복만 하느는 경우
    print("Hello World")

# 리스트 컴프리헨션 쓰지 않고 N X M 크기의 2차원 리스트 초기화 후 값 바꿀 때 발생하는 오류
n = 3
m = 4
array = [[0] * m] * n
print(array)
array[1][2] = 5
print(array)                    # 3개 원소가 한 번에 바뀜 -> 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 레퍼런스로 인식되기 때문

# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본 리스트 : ", a)

a.append(2)                     # 리스트에 원소 삽입
print("삽입 : ", a)

a.sort()                        # 오름차순 정렬
print("오름차순 정렬 : ", a)

a.sort(reverse=True)            # 내림차순 정렬
print("내림차순 정렬 : ", a)

a.reverse()                     # 리스트 원소 뒤집기
print("원소 뒤집기 : ")

a.insert(2, 3)                  # 특정 인덱스에 데이터 추가
print("인덱스 2에 3 추가 : ", a)

b = a.count(3)                  # 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", b)

a.remove(1)                     # 특정 값 데이터 삭제
print("값이 1인 데이터 삭제 : ", a)

# 특정한 값의 원소를 모두 제거하는 방법
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)




