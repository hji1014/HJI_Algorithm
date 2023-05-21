"""

[APPENDIX A - 코딩 테스트를 위한 파이썬 문법]

[5] 입출력
: 알고리즘 문제 풀이의 첫 번째 단계는 데이터를 입력받는 것이다.

<사용법>
def 함수명(매개변수):
    실행할 소스코드
    return 반환 값

"""

# 입력을 위한 전형적인 소스코드
n = int(input())                        # 데이터 개수 입력
data = list(map(int, input().split()))  # 각 데이터를 공백으로 구분하여 입력

data.sort(reverse = True)
print(data)

input()

