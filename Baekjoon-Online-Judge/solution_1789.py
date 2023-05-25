"""
- 문제 설명
: 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

- 입력
: 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

- 출력
: 첫째 줄에 자연수 N의 최댓값을 출력한다.
"""

# 문제해결 방법
#1씩 커지는 등차수열 합을 더하고 S를 넘어갔을 때 값 하나(S랑 같은 값으로 만들어주는 값)를 빼고 전체 개수 N 세기
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print(sum(a))

import time
s = int(input())                    # 입력 : 자연수 N개의 합 S
start_time = time.time()
i = 1
all_N = []
while True:
    all_N.append(i)
    all_sum = sum(all_N)
    if all_sum == s:                # 1부터 1씩 커지는 자연수의 합을 더해가다가 s랑 똑같으면 -> 자연수의 개수 자체가 최대값
        print(len(all_N))
        break
    elif all_sum > s:               # 1부터 1씩 커지는 자연수의 합을 더해가다가 s보다 커지면 -> 자연수의 개수에서 1을 뺀 개수가 최대값
        print(len(all_N) - 1)
        break
    else:
        pass
    i += 1

end_time = time.time()
print(f'실행 시간은 : {end_time - start_time} sec')      # 4,294,967,295이라는 자연수가 들어오면 시간초과 됨

### 블로그 풀이 ###
# https://kongpowder.tistory.com/41
"""
아이디어는 똑같았는데, 정답 풀이는 배열을 안 써서 그런지 시간복잡도 조건을 만족시킴
"""

s = int(input())
count = 0
ans = 0
for i in range(1, s):
    ans += i
    count += 1
    if ans > s:
        count -= 1
        break
print(count)
