sum = 0
temp_time = 0
N = int(input())
times = sorted(list(map(int, (input().split()))))
for time in times:
  temp_time += time 
  sum += temp_time
print(sum)