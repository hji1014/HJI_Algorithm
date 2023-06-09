### 기준에 따라 데이터를 정렬
--------------------------------------------------------------------------------------------------------------------------------  
#### 정렬 알고리즘 개요
	- 정렬(Sorting) : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
 	- 오름차순, 내림차순 등 가장 많이 사용되는 알고리즘 중 하나
  	- 정렬 알고리즘으로 데이터를 정렬 시 다음 장에서 배울 이진 탐색(Binary Search) 가능
   	- 정렬 알고리즘은 이진 탐색의 전처리 과정
	- 선택/삽입/퀵/계수 정렬 다룰 것
	- 파이썬에서 제공하는 기본 정렬 라이브러리를 적용한 효과적인 정렬 수행 방법 학습
	- 정렬 알고리즘을 통해 '알고리즘의 효율성'을 공부할 수 있음
	- 문제에서 요구하는 조건에 따라 적절한 정렬 알고리즘이 공식처럼 사용됨
	- 이 장에서는 오름차순 정렬만 사용
	- Reverse 함수로 내림차순 구현 가능(시간 복잡도 O(N))

--------------------------------------------------------------------------------------------------------------------------------  
#### 선택 정렬
	- 선택 정렬(Selection Sort) : 가장 원시적인 방법으로 매번 '가장 작은 것을 선택'하는 알고리즘
 	  -> 일반적인 오름차순 정렬 시 가장 작은 데이터를 선택해 맨 앞으로 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
	- 스와프 : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
	  -> array[i], array[min_index] = array[min_index], array[i]
	- 시간 복잡도 : O(N^2)
 		i) N = 100 -> 선택 정렬(0.0123초), 퀵 정렬(0.00156초), 기본 정렬 라이브러리(0.00000753초)
		ii) N = 1,000 -> 선택 정렬(0.354초), 퀵 정렬(0.00343초), 기본 정렬 라이브러리(0.0000365초)
		iii) N = 10,000 -> 선택 정렬(15.475초), 퀵 정렬(0.0312초), 기본 정렬 라이브러리(0.000248초)
	  -> 선택 정렬은 기본 정렬 라이브러리에 포함해 뒤에서 다룰 알고리즘과 비교했을 때 매우 비효율적
	  -> 그러나 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코테에서 많으니 익숙해질 필요가 있음

--------------------------------------------------------------------------------------------------------------------------------  
#### 삽입 정렬
	- 삽입 정렬(Insertion Sort) : 특정한 데이터를 적절한 위치에 삽입하는 알고리즘
	  -> 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
	- 선택 정렬과 같이 직관적으로 이해하기 쉬운 알고리즘
	  -> 선택 정렬에 비해 구현 난이도가 높으나, 실행 시간 측면에서 더 효율적
	  -> 데이터가 거의 정렬되어 있을 때 훨씬 효율적
	- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬된 것으로 가정
	- 삽입 정렬은 두 번째 데이터부터 시작(첫 번째 데이터는 그 자체로 정렬되어 있다고 판단)
	- 특정한 데이터가 삽입될 위치를 선정할 때(삽입 위치를 찾기 위해 왼쪽으로 한 칸씩 이동할 때),
	  삽입될 데이터보다 작은 데이터를 처음 만나면 그 위치에서 멈추면 됨
	- 삽입 정렬의 시간 복잡도
	  -> 원칙적으로 삽입 정렬의 시간 복잡도는 O(N^2)
	  -> 최선의 경우 시간 복잡도는 O(N)
	  -> 보통은 삽입 정렬이 퀵 정렬 알고리즘보다 느리지만, 정렬이 거의 되어있을 때 퀵 정렬보다 더 강력

--------------------------------------------------------------------------------------------------------------------------------
#### 퀵 정렬
	- 퀵 정렬은 지금까지 배운 정렬 알고리즘 중 가장 많이 사용되는 알고리즘
	  (이번에는 다루지 않지만 퀵 정렬과 비교할 만큼 빠른 '병합 정렬'알고리즘도 있음)
	- 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘
	  -> 기준을 설정한 다음 큰수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작함 
	- 피벗(Pivot) : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 피벗이라고 함
	- 피벗을 어떻게 설정할 것인지 미리 명시해야 함
	- 이번에는 가장 대표적인 피벗 방식인 호어 분할(Hoare Partition)으로 설명
	- 호어 분할 방식 : 리스트에서 첫 번째 데이터를 피벗으로 정함
	- 호어 분할에 따라 피벗을 설정한 후 왼쪽에서부터 피벗보다 큰 데이터를 찾고,
	  오른쪽에서부터 피벗보다 작은 데이터를 찾아 큰 데이터와 작은 데이터의 위치를 서로 교환해줌
	- 피벗의 왼쪽에는 피벗보다 작은 데이터가 위치하고, 오른쪽에는 피벗보다 큰 데이터가 위치하도록 하는 작업을...
	  -> 분할(Divide) 또는 파티션(Partition)이라고 함
	- 이후 피벗의 왼쪽 리스트와 오른쪽 리스트를 각각 똑같이 피벗을 설정하고 정렬하는 것을 반복하면 전체 정렬이 이루어짐
	- 재귀함수 사용 시 구현이 간결해짐(재귀함수의 종료 조건 : 리스트의 원소가 1개일 때)
	- 퀵 정렬의 시간 복잡도 : O(NlogN) -> 선택/삽입 정렬보다 빠름(일반적으로 컴퓨터 과학에서 logN은 밑이 2인 log를 의미)
	- 하지만 최악의 경우 시간 복잡도가 O(N^2)임
	  -> 최악의 경우 : 이미 데이터가 정렬되어 있는 경우(삽입정렬과 반대)

--------------------------------------------------------------------------------------------------------------------------------
#### 계수 정렬
	- 계수 정렬(Count Sort) : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
	  -> 조건만 부합하다면 사실상 현존하는 정렬 알고리즘 중 기수 정렬(Radix Sort)과 더불어 가장 빠르다고 볼 수 있음
	- ex) 모든 데이터가 양의 정수인 상황일 때...
	  -> 데이터의 개수 : N, 데이터 중 최대값 K일 때 최악의 경우에도 수행시간 O(N+K)를 보장
	- 다만, 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능(실수일 때 사용 불가)
	  -> 모든 범위를 담을 수 있는 크기의 리스트를 선언해야하기 때문
	- 또한 데이터의 최대값과 최소값의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능
	  -> ex) 0 이상 100 이하인 성적 데이터를 정렬할 때 계수 정렬이 효과적
	- 즉, 계수 정렬은 선택/삽입/퀵 정렬과 같이 비교 기반의 정렬 알고리즘이 아님
	- 원리 : 각 데이터가 몇번 등장했는지 count하여 출력

--------------------------------------------------------------------------------------------------------------------------------
#### 정렬 라이브러리
	- 파이썬의 정렬 라이브러리로는 sort(), sorted() 함수가 있음
	- 최악의 경우에도 시간 복잡도 O(NlogN)을 보장함
	- 사실 정렬 라이브러리는 퀵 정렬보다 더욱 효과적
	  -> 병합 + 삽입 정렬의 아이디어를 더한 하이브리드 방식의 정렬 알고리즘으로 구현되어 있음
	- 문제에서 별도의 요구가 없는 한 라이브러리를사용하고, 데이터의 범위가 한정되어 있고 더 빠르게 동작해야할 때는 계수 정렬을 사용하자 
--------------------------------------------------------------------------------------------------------------------------------
#### 예제 설명
		1. 선택 정렬 소스코드
 
 		2. 파이썬 스와프(Swap) 소스코드

		3. 삽입 정렬 소스코드

		4. 퀵 정렬 소스코드

		5. 파이썬의 장점을 살린 퀵 정렬 소스코드

		6. 계수 정렬 소스코드

		7. sorted 소스코드

		8. sort 소스코드

		9. 정렬 라이브러리에서 key를 활용한 소스코드

		10. 위에서 아래로

		11. 성적이 낮은 순서로 학생 출력하기

		12. 두 배열의 원소 교체
		
--------------------------------------------------------------------------------------------------------------------------------
##### [reference]
이것이 취업을 위한 코딩테스트다 with python (나동빈 저) - chapter 06



