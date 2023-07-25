"""

문제 이름 : 빠르게 입력 받기

핵심 : sys.stdin.readline().rstrip() 사용

"""
import sys
# 하나의 문자열 데이터 입력 받기
input_data = sys.stdin.readline().rstrip()

# 입력 받은 문자열 그대로 출력
print(input_data)