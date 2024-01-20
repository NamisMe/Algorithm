string = input()
result = 0
expr = string.split("-")

#맨 처음 부분
result += sum(map(int, expr[0].split("+")))

# 빼줄 부분
for i in range(1, len(expr)):
  result -= sum(map(int, expr[i].split("+")))
print(result)