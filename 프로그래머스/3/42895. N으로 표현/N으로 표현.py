def calculate(X, Y):
    num_set = set()
    for x in X:
        for y in Y:
            num_set.add(x+y)
            num_set.add(x-y)
            num_set.add(x*y)
            if y != 0:
                num_set.add(x//y)
    return num_set

def solution(N, number):
    answer = -1 # 일단 -1로 초기화
    result_dp = {} 
    result_dp[1] = {N} # key: 숫자 사용횟수, value: 숫자를 key번 사용했을 때 나오는 연산 결과 set
    if N == number : # N을 1번 사용하면 그냥 N
        return 1
    for n in range(2, 9):
        i = 1
        temp_set = {int(str(N)*n)} # N = 5, 2번 사용할 때 먼저 55를 저장
        #  1 (op) N-1 ... n-1 (op) 1 까지 계산
        while i < n :
            temp_set.update(calculate(result_dp[i], result_dp[n-i]))
            # print(f"i:{i}, n:{n}, len:{(temp_set)}")
            i += 1
        if number in temp_set:
            answer = n 
            break 
        
        result_dp[n] = temp_set
    return answer 
    