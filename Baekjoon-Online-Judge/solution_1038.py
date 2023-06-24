"""
[감소하는 수]
"""
n = int(input())

if n // 10 == 0:
    print(n)
    exit(0)

count = 0
arr = []
while True:
    for i in range(1000000):
        now = 10e9
        state = False
        if i < 10:
            arr.append(i)
            count += 1
        elif i >= 10:
            for j in str(i):
                if int(j) < now:
                    now = int(j)
                    state = True
                elif int(j) >= now:
                    state = False
            if state == True:
                count += 1
                arr.append(i)
        print(i)
        if count == n:
            break
