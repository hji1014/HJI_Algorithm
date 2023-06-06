"""
[회전 초밥]
"""
# 내 풀이
"""
틀린 이유 : 초밥 벨트가 원형이므로 뒤에서 3개 원소랑 맨앞의 하나의 원소가 세트가 될 수 있음
"""
n, d, k, c = map(int, input().split(' '))       # 입력 받기
belt = []
for i in range(n):
    belt.append(int(input()))

start = belt[0:k-1]                             # 초밥 벨트 첫 세 원소로 배열 만듦
max = 0                                         # 최댓값 초기화

for i in range(n - k + 1):                      # 초밥 벨트 중 처음 세 원소 뺀 나머지로 반복문
    start.append(belt[k + i - 1])               # 세 원소 이후 초밥 추가
    plus_cp = start + [c]                       # 쿠폰 초밥 추가
    food_set = set(plus_cp)                     # set으로 중복 원소 제거
    if len(food_set) > max:                     # food_set의 길이가 max 보다 클 때
        max = len(food_set)                     # max 업데이트
    del start[0]                                # start 배열 첫 번째 원소 제거

print(max)

# 블로그 풀이
"""
Pypy3로 돌려야 시간초과 안 뜲 -> 삼성 코테는 Pypy3로 채점하기 때문에 가능
ref : https://velog.io/@study-dev347/%EB%B0%B1%EC%A4%80-2531-%ED%9A%8C%EC%A0%84-%EC%B4%88%EB%B0%A5
"""
n, d, k, c = map(int, input().split(' '))       # 입력 받기
belt = []
for i in range(n):
    belt.append(int(input()))
lp, rp = 0, 0
answer = 0

while lp != n:
    rp = lp + k
    case = set()
    for i in range(lp, rp):
        i = i % n               # 이게 핵심 -> sliding window ★★★★★★
        case.add(belt[i])
    case.add(c)                 # 쿠폰 메뉴 추가
    cnt = len(case)
    answer = max(answer, cnt)
    lp += 1

print(answer)
