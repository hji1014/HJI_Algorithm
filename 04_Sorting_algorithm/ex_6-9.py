"""

문제 이름 : 정렬 라이브러리에서 key를 활용한 소스코드

핵심 : 람다(lambda) 함수 사용 시 편함

"""
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

result = sorted(array, key=lambda x : x[1])
print(result)