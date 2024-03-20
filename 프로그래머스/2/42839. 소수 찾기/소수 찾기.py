import math
from itertools import permutations, combinations
def solution(numbers):
    num_set = set()
    # 소수 판별 함수
    def is_prime_number(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False # 소수가 아님
        return True # 소수임
    for i in range(1, len(numbers)+1):
        for p in list(permutations(numbers, r = i)):
            num_set.add(int(''.join(p)))
    answer = 0
    for number in num_set:
        if is_prime_number(number) == True:
            answer += 1
    return answer