"""
[프린터 큐]
ref :
"""
# 내 풀이
case_num = int(input())
for _ in range(case_num):
    n, m = map(int, input().split(' '))
    imp = list(map(int, input().split(' ')))
    docs = list(range(n))       # 문서 수만큼 차례로 번호 매기기
    max_imp = max(imp)          # 중요도 최댓값 초기화
    order = []                  # 프린트되는 문서 순서 저장 배열 초기화
    iterable = True             # while문 조건
    while iterable:
        docs_num = docs[0]      # 처음 문서부터 확인
        if imp[docs.index(docs_num)] >= max_imp:    # 확인 중인 문서의 중요도가 가장 크면,
            order.append(docs_num)                  # 프린트 순서 저장 배열에 추가
            del docs[0]                             # 문서 제거
            del imp[0]                              # 문서의 중요도 제거
            if len(imp) != 0:                       # 중요도 배열의 크기가 0이 아니면...
                max_imp = max(imp)                  # 중요도 최댓값 업데이트
        elif imp[docs.index(docs_num)] < max_imp:   # 확인 중인 문서의 중요도가 가장 크지 않으면,
            imp.append(imp[0])                      # 중요도 맨 뒤에 현재 중요도 옮김
            del imp[0]                              # 위에서 옮긴 맨 앞의 중요도 제거
            del docs[0]                             # 현재 문서 제거
            docs.append(docs_num)                   # 현재 문서 맨 뒤에 추가
        if len(order) == n:                         # 모든 문서의 순서가 정해지면,
            iterable = False                        # while문 종료
    print(order.index(m) + 1)                       # 순서가 궁금했던 문서의 번호 출력