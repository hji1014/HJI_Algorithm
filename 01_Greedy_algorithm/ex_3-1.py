"""
문제 이름 : 거스름돈

핵심 : 가장 큰 화폐 단위부터'돈을 거슬러 주는 것
-> 최소의 동전 개수로 모두 거슬러 줄 수 있음

"""
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin              # 해당 화폐로 거슬러 줄 수 있는 동전의 수 세기
    n %= coin                       # 거슬러주고 남은 돈으로 변환

print(count)