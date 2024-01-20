import sys
input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

#우선 그냥 첫번째를 min_cost, min_price로 잡는다.
min_cost = prices[0] * dists[0]
min_price = prices[0]

# (양쪽 끝을 제외하고) 1부터 N-1까지 돌면서
for index in range(1, N - 1):
    if min_price > prices[index]:
        min_price = prices[index]
    min_cost += min_price * dists[index]

print (min_cost)