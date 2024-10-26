import math
def solution(r1, r2):
    count = 0
    
    # x를 0부터 r2까지 반복
    for x in range(1, r2 + 1): # 정수
        # 큰 원의 조건에 맞는 최대 y값
        max_y = int(math.sqrt(r2**2 - x**2))
        
        # 작은 원의 조건에 맞는 최소 y값 (음수인 경우 0으로 처리)
        min_y = math.ceil(math.sqrt(r1**2 - x**2)) if x**2 < r1**2 else 0
        # 해당 x 값에 대해 가능한 y 값의 개수를 더함
        count += (max_y - min_y + 1)
        
    
    # 모든 사분면의 좌표를 고려해 4배로 계산
    return count * 4