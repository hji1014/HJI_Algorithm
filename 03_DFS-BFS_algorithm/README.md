### 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘 - DFS / BFS
--------------------------------------------------------------------------------------------------------------------------------  
#### 꼭 필요한 자료구조 기초
	- 탐색(Search) : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
	  -> 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룸
	  -> 대표적인 탐색 알고리즘으로 DFS와 BFS가 있음
	  -> DFS/BFS를 사용하기 위해 기본 자료구조인 '스택'과 '큐'를 이해하고 '재귀 함수'를 알아야 함
	  
	- 자료구조(Data Structure) : 데이터를 표현하고 관리하고 처리하기 위한 구조
	
	- 스택과 큐는 다음과 같은 두 개의 핵심적인 함수로 구성됨
	
		* 삽입(Push) : 데이터를 삽입
		* 삭제(Pop) : 데이터를 삭제
		
	- 스택과 큐에서 삽입/삭제 뿐만 아니라 오버플로와 언더플로를 고려해야 함
	
		* 오버플로(Overflow) : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산 시 발생
		* 언더플로(Underflow) : 특정한 자료구조에 데이터가 전혀 없는 상태에서 삭제 연산 수행 시 발생
	
	- 스택(Stack) : 박스 쌓기로 생각할 수 있음 -> First In Last Out (FILO, 선입후출 구조)
	  -> 리스트를 기준으로 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작
	
	- 큐(Queue) : 대기 줄로 생각할 수 있음 -> First In First Out (FIFO, 선입선출 구조)
	  -> collections 모듈에서 제공하는 deque 자료구조 활용하면 됨
	  
	- 재귀 함수(Recursive Function) : 자기 자신을 다시 호출하는 함수
	  -> 재귀 함수의 종료 조건 : 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 함
	  
		- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용
		  -> 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
		- 즉, 재귀 함수는 내부적으로 스택 자료구조와 동일함
		- 재귀 함수를 이용하는 대표적 예제로는 팩토리얼(Factorial) 문제가 있음
	
--------------------------------------------------------------------------------------------------------------------------------  
#### 탐색 알고리즘 DFS / BFS	
	- 그래프(Graph) : 그래프는 '노드(Node)'와 '간선(Edge)'으로 표현됨
		* 노드(Node)=정점(Vertex)
		* 두 노드가 간선으로 연결되어 있으면 '두 노드는 인접하다(Adjacent)'라고 표현
		
		- 프로그래밍으로 그래프를 표현하는 방법은 2가지가 있음
			* (1) 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
			* (2) 인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식
		- 두 방식의 차이
			* 메모리 측면 : 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 낭비됨
			* 속도 측면 : 인접 리스트 방식은 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림
			
	- DFS (Depth First Search, 깊이 우선 탐색) : 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
	
		- 깊이 우선 탐색 알고리즘으로써 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후,
		  다시 돌아가 다른 경로로 탐색하는 알고리즘
		- 스택 자료구조를 이용함
		- 동작 과정
			1) 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
			2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 함,
			  방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
			3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
		- 시간 복잡도 : O(N)
	
	- BFS (Breadth First Search, 너비 우선 탐색) : 가까운 노드부터 탐색하는 알고리즘
	
		- BFS 구현에서는 선입선출 방식인 '큐' 자료구조를 이용하는 것이 정석임
		- 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어,
		  가까운 노드부터 탐색을 진행함
		- 동작 과정
			1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
			2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함
			3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
		- 시간 복잡도 : O(N)
		- 보통 코딩 테스트에서는 보통 DFS보다 BFS 구현이 조금 더 빠르게 동작
	
--------------------------------------------------------------------------------------------------------------------------------
#### 예제 설명
		1. 스택 예제
		
		2. 큐 예제
		
		3. 재귀 함수 예제
		
		4. 재귀 함수 종료 예제
		
		5. 2가지 방식으로 구현한 팩토리얼 예제
		
		6. 인접 행렬 방식 예제
		
		7. 인접 리스트 방식 예제
		
		8. DFS 예제
		
		9. BFS 예제
		
		10. 음료수 얼려 먹기
		
		11. 미로 탈출
		
--------------------------------------------------------------------------------------------------------------------------------
##### [reference]
이것이 취업을 위한 코딩테스트다 with python (나동빈 저) - chapter 05


