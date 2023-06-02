"""

문제 이름 : 재귀 함수 예제

핵심 : 함수 내부에 자기 함수를 다시 불러오는 구조
->

"""
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# 이렇게 하면 몇 번 호출되다가 오류가 발생