"""
[N번째 큰 수]
"""

# 내 풀이 (1) - 메모리 초과
"""
틀린 이유 : data_1d의 크기가 너무 커지면 메모리가 초과되는 것 같음
"""
#n = int(input())
#data = []
#for _ in range(n):
#    data.append(list(map(int, input().split(' '))))

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2075.txt')
n = int(f.readline().rstrip())
data = []
for _ in range(n):
   data.append(list(map(int, f.readline().rstrip().split(' '))))
f.close()

if len(data) == 1:
    print(data[0])
    exit(0)

data_1d = []

for i in data:
    for j in i:
        data_1d.append(j)

data_1d.sort(reverse=True)

print(data_1d[n - 1])

# 내 풀이 (2) - 메모리 초과
"""
틀린 이유 : data_1d의 크기를 5로 제한하여도 메모리가 초과됨.
"""
#n = int(input())
#data = []
#for _ in range(n):
#    data.append(list(map(int, input().split(' '))))

f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2075.txt')
n = int(f.readline().rstrip())
data = []
for _ in range(n):
   data.append(list(map(int, f.readline().rstrip().split(' '))))
f.close()

if len(data) == 1:
    print(data[0])
    exit(0)

data_1d = []

for i in data:
    for j in i:
        if len(data_1d) < n:
            data_1d.append(j)
        if len(data_1d) >= n:
            if j > min(data_1d):
                data_1d.remove(min(data_1d))
                data_1d.append(j)
            else:
                pass

data_1d.sort()

print(data_1d[0])

# 블로그 풀이
"""
ref : https://kjhoon0330.tistory.com/entry/BOJ-2075-N%EB%B2%88%EC%A7%B8-%ED%81%B0-%EC%88%98-Python
우선순위 큐를 사용해야 함
"""
