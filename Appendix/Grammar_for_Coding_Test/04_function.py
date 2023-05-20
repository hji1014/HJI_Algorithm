"""

[APPENDIX A - 코딩 테스트를 위한 파이썬 문법]

[4] 함수
: 똑같은 코드를 반복적으로 사용할 때를 위해 사용하는 방법이다. 코딩 테스트에서 테스트 케이스가 입려된 뒤에 테스트 케이스만큼 특정한 알고리즘을 수행한 결과를 반복적으로 출력해야하기 때문에 함수를 쓰는 것이 중요하다.

<사용법>
def 함수명(매개변수):
    실행할 소스코드
    return 반환 값

"""

# 더하기 기능을 제공하는 함수
def add(a, b):
    return a + b

print(add(3, 7))

# return문 없는 더하기 함수
def add(a, b):
    print('함수의 결과 : ', a + b)

print(add(3, 7))
print(add(b=1000, a=200))       # 함수를 호출하는 과정에서 인자(argument)를 넘겨줄 때, 파라미터의 변수를 직접 지정해서 값을 넣을 수 있다. 순서가 바뀌어도 상관없다는 것이 특징이다.

# 함수 밖의 변수 데이터를 변경해야 하는 경우 -> global 키워드 사용
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 람다 표현식(lambda express)을 사용하여 함수를 간단히 구현하기
print((lambda a, b: a + b)(3, 7))
#a = (lambda a, b: a + b)(3, 7)
