"""
- 문제 설명
: 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

- 입력
: 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
- 출력
: 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
"""
# 접근방식
# 최대한 큰 음수로 가게해야할 거 같음
# 입력은 문자열로 들어오는 것인가? 아마 그럴 듯
# 정수들로 쪼개서 리스트에 저장
# -(ㅁ+ㅁ)으로 묶어야 함
# - 가 있고 그 다음이 +인 경우에 그 다음꺼를 -로 바꾸면 될 듯?

expression = input()
sp = list(''.join(expression))      # sp = list(expression)으로 쓰면 됨. join은 의미 없음
num = []
temp = ''

# 정수 리스트 생성
for i in sp:
    if i == '+' or i == '-':
        num.append(int(temp))
        temp = ''
        temp += i
    else:
        temp += i
num.append(int(temp))

ans = 0
if '-' not in sp:
    ans = sum(num)
    print(ans)
else:
    for i in range(len(num)):
        if i == 0:
            ans += num[i]
        elif i > 0 and num[i - 1] < 0:
            ans -= num[i]
        elif i > 0 and num[i - 1] > 0:
            ans += num[i]
        else:
            pass
    print(ans)

# 블로그 풀이
"""
ref : https://pacific-ocean.tistory.com/228
핵심 : -다음 +가 나왔을 때 다음꺼만을 바꾸는 것이 아니라, -다음 +가 나오는 모든 수를 -로 해야함
즉, -로 끊은 다음에 리스트에 담고 각 원소의 수식을 계산한 후 첫 번째 수에서 나머지 모든 수를 빼주면 됨
"""
expression = input().split('-')
num = []

for i in expression:
    temp = 0
    s = i.split('+')
    for j in s:
        temp += int(j)
    num.append(temp)

ans = num[0]

for i in range(1, len(num)):
    ans -= num[i]

print(ans)
