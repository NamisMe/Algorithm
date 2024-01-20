N = int(input())
t, p, dp = list(), list(), list()
for _ in range(N):
  t_i, p_i = map(int, input().split())
  t.append(t_i)
  p.append(p_i)
  dp.append(0)
dp.append(0) # 8일째의 값은 0으로 박아버리기 .

for index in range(N -1 , -1, -1): # 역순으로 돌겠다.
  if (t[index] + index) > N : #현재 날짜 + 걸리는 시간이 퇴사 날을 넘어간다면
    dp[index] = dp[index+1] # 다음 날의 dp값을 그대로 가져오겠다.
  else:
    dp[index] = max(dp[index+1], p[index] + dp[index + t[index]])

print(dp[0])