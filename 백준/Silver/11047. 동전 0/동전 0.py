N, K = map(int, input().split()) # N : 화폐 종류 수 , K: 거슬러줄 돈 
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

count = 0
for coin in coins:
  if K >= coin:
    count += K // coin
    K %= coin 
    if K <= 0:
      break
print(count)