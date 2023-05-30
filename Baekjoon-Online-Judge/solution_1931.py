"""
- 문제 설명
: 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

- 입력
: 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

- 출력
: 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
"""
# 아이디어가 생각이 안 남...

n = int(input())
meeting_time = []
for i in range(n):
    meeting_time.append(list(map(int, input().split(''))))

n = 11
meeting_time = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]]

count = 0
start = min([i[0] for i in meeting_time])
end = max([i[1] for i in meeting_time])

mt_range = []
for i in meeting_time:
    mt_range.append([j for j in range(i[0], i[1] + 1)])

# 블로그 풀이
"""
ref : https://jokerldg.github.io/algorithm/2021/03/11/meeting-room.html
핵심 : 먼저 시작 시간을 오름차순으로 정렬한 뒤, 끝나는 시간을 기준으로 한번 더 정렬을 해야 한다.
왜? -> 끝나는 시간이 같을 때 이미 시작 시간의 오름차순으로 정렬이 되어 있으니...
a1 = sorted(meeting_time, key=lambda a: a[0])
a2 = sorted(a1, key=lambda a: a[1])
b1 = sorted(meeting_time, key=lambda a:a[1])
a2와 b1은 같지 않나?
반례 ->
"""
n = int(input())
meeting_time = []
for i in range(n):
    meeting_time.append(list(map(int, input().split(' '))))
meeting_time.sort(key=lambda a: a[0])
meeting_time.sort(key=lambda a: a[1])
last = 0
count = 0
for i, j in meeting_time:
    if i >= last:
        count += 1
        last = j
print(count)