"""

문제 이름 : 왕실의 나이트

핵심 :
->

"""
# 내 코드
import sys
start_location = sys.stdin.readline().rstrip()

column_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}      # 'a1', 'c2' 등의 입력을 [1, 1], [3, 2]의 리스트로 변환
m1 = [[1, 2], [-1, 2], [1, -2], [-1, -2]]                                   #
m2 = [[2, 1], [-2, 1], [2, -1], [-2, -1]]
for i in column_dict.keys():
    if i in start_location:
        location_convert = [column_dict[i], int(start_location[1])]

count = 0
for i in m1:
    expected_location = []
    expected_location = [location_convert[0] + i[0], location_convert[1] + i[1]]
    if expected_location[0] < 1 or expected_location[0] > 8 or expected_location[1] < 1 or expected_location[1] > 8:
        continue
    count += 1
for i in m2:
    expected_location = []
    expected_location = [location_convert[0] + i[0], location_convert[1] + i[1]]
    if expected_location[0] < 1 or expected_location[0] > 8 or expected_location[1] < 1 or expected_location[1] > 8:
        continue
    count += 1

print(count)

# 책 코드 - 더 효율적
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1    # 간단한 방법을 통해 입력의 row, column 구함

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]    # 8가지 경우의 수 선언

result = 0
for step in steps:                          # 8가지 경우의 수를 각각 적용하여 체스판 안에 있는지 확인
    next_row = row + step[0]                # 각 경우의 수를 적용하였을 때 좌표 계산
    next_column = column + step[1]
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:    # 다음 좌표가 체스판 안에 있으면...
        result += 1                                                                 # 가능한 경우의 수 하나 증가

print(result)