"""

[APPENDIX A - 코딩 테스트를 위한 파이썬 문법]

[3] 반복문
: 특정한 소스코드를 반복적으로 실행하고자 할 때 사용할 수 있다. 코딩 테스트에서의 실제 사용 예시를 확인해보면, 대부분의 경우에서 for문이 더 소스코드가 짧은 경우가 많다.

1-1) while문

1-2) for문

"""

### while문 ###

# 1부터 9까지 각 정수의 합을 계산하는 코드
i = 1
result = 0

while i <= 9:
    result += i
    i += 1
    # break로 조건문에서 나올 수 있음
    #if i == 2:
    #    break

print(result)

# 1부터 9까지의 정수 중 홀수만 더하는 코드 (내 코드)
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
        i += 1
    else:
        i += 1

print(result)

# 1부터 9까지의 정수 중 홀수만 더하는 코드 (책 코드)
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

### for문 ###

# 1부터 9까지 각 정수의 합을 계산하는 코드
result = 0

for i in range(1, 10):
    result += i

print(result)

# 학생 5명의 합격 여부를 판단하는 프로그램
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        #print(i + 1, "번 학생은 합격입니다.")
        print("축하합니다! %d번 학생은 합격입니다." % (i + 1))        # 이렇게 문자열 중간에 수 자료형 넣을 수 있음

# 2명 블랙리스트가 있을 때 학생 5명의 합격 여부를 판단하는 프로그램
scores = [90, 85, 77, 65, 97]
cheating_list = [2, 4]

for i in range(5):
    if (i + 1) in cheating_list:
        continue
    if scores[i] >= 80:
        print("축하합니다! %d번 학생은 합격입니다." % (i + 1))

# 2중 반복문 사용하여 구구단 계산하는 프로그램
for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j))
        if i == 9 and j == 9:
            print("구구단 끝!")
