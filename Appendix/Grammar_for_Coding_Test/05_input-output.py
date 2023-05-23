"""

[APPENDIX A - 코딩 테스트를 위한 파이썬 문법]

[5] 입출력
: 알고리즘 문제 풀이의 첫 번째 단계는 데이터를 입력받는 것이다.

<반드시 알고 있어야 하는 method>

# 입력받은 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드
data = list(map(int, input().split()))

"""

# 입력을 위한 전형적인 소스코드
n = int(input())                        # 데이터 개수 입력 -> 줄바꿈이 필요할 때 이 함수를 여러 번 쓰면 됨
data = list(map(int, input().split()))  # 각 데이터를 공백으로 구분하여 입력
                                        # map(function, interable) : funtion은 함수이고 '()'를 쓰지 않는다
                                        #                            iterable에는 반복 가능한 자료형(리스트, 튜플)
                                        # 여기서는 input().split으로 공백을 사용하여 입력 받고 입력 받은 값을 리스트로 생성
                                        # map() : 리스트의 요소를 지정된 함수로 처리해주는 함수 -> 리스트의 모든 요소를 한 번에 정수형으로 변경

data.sort(reverse = True)
print(data)

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())
print(n)
print(m)
print(k)

# 입력의 개수가 굉장히 많은 경우 (cf. input() 함수는 동작 속도가 느림)
import sys
data = sys.stdin.readline().rstrip()        # 이거를 정수형 리스트로 바꿀려면...?
print(data)

# 변수 출력 예시
a = 1
b = 2
print(a, b)
print(a)
print(b)

# 출력 시 오류가 발생하는 소스코드 예시
answer = 7
print("정답은" + answer + "입니다.")          # str은 str끼리 더할 수 있으므로 int형인 answer를 str형으로 바꾸어야 함
print("정답은" + str(answer) + "입니다.")     # 정답
print("정답은 %d입니다." % answer)            # 대체 방법 (1)
print(f"정답은 {answer}입니다.")              # 대체 방법 (2) -> f-string 문법
