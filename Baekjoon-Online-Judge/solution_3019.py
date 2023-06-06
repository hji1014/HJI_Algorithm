"""
[테트리스]
ref : https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-3019%EB%B2%88-%ED%85%8C%ED%8A%B8%EB%A6%AC%EC%8A%A4-%EC%B4%88%EC%BD%94%EB%8D%94
"""
c, p = map(int, input().split(' '))
h = list(map(int, input().split(' ')))

answer = 0
if p == 1:
    answer += c                     # c 자체가 경우의 수
    for i in range(c - 3):          # c-3과 같이 range안에 들어갈 정수 생각하는 것이 중요!!
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2] and h[i + 2] == h[i + 3]:          # 0000
            answer += 1

elif p == 2:
    for i in range(c - 1):
        if h[i] == h[i + 1]:                                                            # 00
            answer += 1

elif p == 3:
    for i in range(c - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2] - 1:                               # 001
            answer += 1
    for i in range(c - 1):
        if h[i] == h[i + 1] + 1:                                                        # 10
            answer += 1

elif p == 4:
    for i in range(c - 2):
        if h[i] == h[i + 1] + 1 and h[i + 1] == h[i + 2]:                               # 100
            answer += 1
    for i in range(c - 1):
        if h[i] == h[i + 1] - 1:                                                        # 01
            answer += 1

elif p == 5:
    for i in range(c - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]:                                   # 000
            answer += 1
        if h[i] == h[i + 1] + 1 and h[i + 1] + 1 == h[i + 2]:                           # 101
            answer += 1
    for i in range(c - 1):
        if h[i] == h[i + 1] - 1:                                                        # 01
            answer += 1
        if h[i] == h[i + 1] + 1:                                                        # 10
            answer += 1

elif p == 6:
    for i in range(c - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]:  # 000
            answer += 1
        if h[i] == h[i + 1] + 1 and h[i + 1] == h[i + 2]:  # 011
            answer += 1
    for i in range(c - 1):
        if h[i] == h[i + 1]:  # 00
            answer += 1
        if h[i] == h[i + 1] + 2:  # 20
            answer += 1

elif p == 7:
    for i in range(c - 2):
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2]:  # 000
            answer += 1
        if h[i] == h[i + 1] and h[i + 1] == h[i + 2] - 1:  # 110
            answer += 1
    for i in range(c - 1):
        if h[i] == h[i + 1]:  # 00
            answer += 1
        if h[i] == h[i + 1] - 2:  # 02
            answer += 1

print(answer)