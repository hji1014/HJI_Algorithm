"""
[분수찾기]
"""
x = int(input())
num = 0

for i in range(1, 10000000):
    num += i
    if num > x:
        num -= i
        break
    elif num == x:
        break

add = x - num - 1

if add == -1:
    if i % 2 == 1:
        a = i
        b = 1
    elif i % 2 == 0:
        a = 1
        b = i
else:
    a = i - (1 * add)
    b = 1 + (1 * add)

if i % 2 == 1:
    print(str(a) + '/' + str(b))
elif i % 2 == 0:
    print(str(b) + '/' + str(a))