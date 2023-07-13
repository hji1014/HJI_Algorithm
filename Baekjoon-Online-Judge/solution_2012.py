"""
[등수 매기기]
"""
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

check = [False] * n
unsatisfied = 0

for i in range(len(data)):
    if check[data[i] - 1] == False:
        check[data[i] - 1] = True
    else:
        for j in range(len(check)):
            if check[j] == False:
                check[j] = True
                unsatisfied += abs(data[i] - (j + 1))
                break

print(unsatisfied)