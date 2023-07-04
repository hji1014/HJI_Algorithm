"""
[수 묶기]
"""
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)                 # 입력값을 내림차순으로 정렬

temp_plus = []                          # 양수 저장 배열(1, 0 제외)
temp_minus = []                         # 음수 저장 배열
new_data = []                           # 곱한값과 나머지 수열 저장
for i in data:
    if i > 1:                           # i가 양수일 때 temp_plus 배열에 하나씩 저장
        temp_plus.append(i)
        if len(temp_plus) == 2:         # temp_plus가 2개가 될 때 2개 값을 곱하여 new_data에 저장
            new_data.append(temp_plus[0] * temp_plus[1])
            temp_plus = []              # 2개가 되면 곱한값 저장 후 초기화
    if i == 1 or i == 0:                # 데이터가 1 또는 0일 때 그대로 저장
        new_data.append(i)

data.reverse()                          # 음수 다루는 방법이 중요!!
for i in data:
    if i < 0:                           # i가 음수일 때 temp_minus 배열에 하나씩 저장 -> 음수값은 오름차순으로 진행해야함
        temp_minus.append(i)
        if len(temp_minus) == 2:        # temp_minus가 2개가 될 때 2개 값을 곱하여 new_data에 저장
            new_data.append(temp_minus[0] * temp_minus[1])
            temp_minus = []

if len(temp_plus) == 1:                 # 반복문이 끝난 후 양수 배열의 길이가 1이면 그대로 저장
    new_data.append(temp_plus[0])
if len(temp_minus) == 1:                # 반복문이 끝난 후 음수 배열의 길이가 1이고...
    if 0 in new_data:                   # 0이 new_data에 있다면 버리기 (어차피 곱하면 0)
        pass
    else:                               # 0이 new_data에 없다면 new_data에 저장
        new_data.append(temp_minus[0])

print(sum(new_data))