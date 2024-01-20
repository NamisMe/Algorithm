N = int(input())
rankings = [int(input()) for _ in range(N)]
min_ranking = 0
sorted_rankings = sorted(rankings)
for i in range(N):
  min_ranking += abs(sorted_rankings[i] - (i+1))
print(min_ranking)