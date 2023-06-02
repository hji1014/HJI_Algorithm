"""

문제 이름 : 재귀 함수 종료 예제

핵심 : 종료 조건을 꼭 명시해야 함
->

"""
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 조건 명시
    if i == 100:
        return
    print(f'{i}번째 재귀 함수에서 {i+1}번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(f'{i}번째 재귀 함수를 종료합니다.')

recursive_function(1)