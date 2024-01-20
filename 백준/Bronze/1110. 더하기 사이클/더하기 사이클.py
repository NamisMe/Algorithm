N = int(input())
update_num = N
count = 0

while True:
    a = update_num // 10
    b = update_num % 10
    c = (a + b) % 10
    update_num = b * 10 + c
    count += 1
    if update_num == N:
        break

print(count)