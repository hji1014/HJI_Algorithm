"""

[신입 사원]

- 문제 설명
: 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.
그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

- 입력
: 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

- 출력
: 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.

"""
# 접근 방식
# 1차 점수를 오름차순으로 정렬 후 2차 점수를 위에서부터 나머지 2차 점수와 비교
# 둘 다 떨어지면 탈락

# 내 풀이 (1) -> 시간 초과 뜨는 중
t = int(input())
ans = []
for i in range(t):
    n = int(input())
    data = []
    count = 0
    for j in range(n):
        data.append(list(map(int, input().split(' '))))
    data_sorted = sorted(data, key=lambda x : x[0], reverse=True)
    for j, k in data_sorted:
        if j == 1:
            pass
        else:
            count += 1
            if k > min([i[1] for i in data_sorted[count:]]):    # min() 함수 문제
                n -= 1
            else:
                pass
    ans.append(n)

for i in ans:
    print(i)

# 내 풀이 (2) -> 블로그 풀이 참고함 -> 아직도 시간초과 뜸
"""
ref : https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1946-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90-%EC%8B%A4%EB%B2%841-%EA%B7%B8%EB%A6%AC%EB%94%94
"""
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    data = []
    top = 0
    result = 1          # 서류 1등은 무조건 됨
    for j in range(n):
        data.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    data_sorted = sorted(data, key=lambda x: x[0])
    for j in range(1, len(data_sorted)):
        if data_sorted[j][1] < data_sorted[top][1]:
            top = j
            result += 1
    print(n)
