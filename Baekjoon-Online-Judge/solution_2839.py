"""
- 문제 설명
: 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

- 입력
: 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

- 출력
: 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
"""

# 문제해결 방법
"""
1) 3보다 작을 때
2) 3으로 나누어 떨어질 때
3) 5로 나누어 떨어질 때
4) 5로 나누고 나머지가 3으로 떨어질 때
5) 5로 나누고 나머지가 3으로 떨어지지 않을 때

1) 5보다 작을 때
    1-1) 3일때
        answer = 1
    1-2) 3이 아닐 때
        answer = -1
2) 5보다 크거나 같을 때
    2-1) 5로 나누어 떨어질 때
        answer = N / 5
    2-2) 5로 나누어 떨어지지 않을 때
        2-2-1) 3으로 나누어 떨어질 때
            answer = N / 3
        2-2-2) 3으로 나누어 떨어지지 않고, 5로 나누고 나머지가 3으로 떨어질 때
            answer = (N // 5) + ((N - (5 * (N // 5))) // 3)
        2-2-2) 다 아닐 때
            answer = -1
"""

def solution(N):

    answer = 0

    if N < 5:
        if N == 3:
            answer = 1
        else:
            answer = -1
    else:
        if N % 5 == 0:
            answer = int(N / 5)
        else:
            if N % 3 != 0 and (N % 5) % 3 == 0:
                answer = (N // 5) + ((N % 5) // 3)
                answer = int(answer)
            elif N % 3 == 0 and (N % 5) % 3 == 0:
                answer = (N // 5) + ((N % 5) // 3)
                answer = int(answer)
            elif N % 3 != 0 and (N % 5) % 3 != 0:
                tmp = []
                for i in range(1, ((N // 5) + 1)):
                    if (N % i * 5) % 3 == 0:
                        tmp.append(i)
                    else:
                        pass
                answer = max(tmp) + ((N - (5 * max(tmp))) / 3)
                answer = int(answer)
            elif N % 3 == 0 and (N % 5) % 3 != 0:
                tmp = []
                for i in range(1, ((N // 5) + 1)):
                    if (N % i * 5) % 3 == 0:
                        tmp.append(i)
                    else:
                        pass
                if len(tmp) != 0:
                    answer = max(tmp) + ((N - (5 * max(tmp))) / 3)
                    answer = int(answer)
                else:
                    answer = int(N / 3)
            else:
                answer = -1

    return answer

N = 9
solution(N)

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #

### 블로그 풀이 ###
sugar = int(input())
bag = 0

while sugar >= 0:               # sugar가 0보다 클 때 반복
    if sugar % 5 == 0:          # sugar가 5의 배수일 때...
        bag += (sugar // 5)     # 5kg 봉지 수 구하기
        print(bag)              # bag 변수에 5kg 봉지 수 추가
        break                   # while문 종료(else로 가지 않음)
    sugar -= 3                  # sugar가 5의 배수가 아니면 sugar에 -3kg 반복
    bag += 1                    # sugar에서 -3kg 했으니까 bag에 3kg 봉지 개수 하나 추가
else:               # sugar가 0보다 작아지면 else문으로 내려감
    print(-1)       # -1이 출력되고 종료
