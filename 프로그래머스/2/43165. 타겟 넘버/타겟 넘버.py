# 쌩 구현

from itertools import product
import time
def solution(numbers, target):
    start = time.time()
    num_length = len(numbers)
    # 전체 가능한 case 구하기
    cases = []
    for _ in range(num_length):
        cases.append([-1,1])
    cases = list(product(*cases))
    # 전체 cases 돌면서 확인하기 
    count = 0
    for case in cases:
        s = 0
        for i in range(num_length):
            s += case[i] * numbers[i]
            
        if s == target: # 더한 값이 target과 같으면
            count += 1
    print(time.time() - start)
    return count
