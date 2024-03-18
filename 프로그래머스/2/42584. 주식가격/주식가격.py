def solution2(prices):
    # 결과를 저장할 배열의 길이를 prices의 길이와 동일하게 초기화합니다.
    answer = [0] * len(prices)
    
    # prices 배열을 순회합니다.
    for i in range(len(prices)):
        # 현재 가격부터 배열의 끝까지 비교합니다.
        for j in range(i+1, len(prices)):
            # 가격이 떨어지지 않은 기간을 1초 증가시킵니다.
            answer[i] += 1
            # 만약 가격이 떨어진 경우, 더 이상 비교할 필요가 없으므로 반복문을 종료합니다.
            if prices[i] > prices[j]:
                break
    
    # 계산된 결과를 반환합니다.
    return answer

def solution1(prices):
    # 가격이 떨어지지 않은 기간을 저장할 배열
    answer = [0] * len(prices)
    # 가격이 떨어지지 않은 시점들을 저장할 스택
    stack = []
    
    # prices 배열을 순회합니다.
    for i, price in enumerate(prices):
        # 스택이 비어있지 않고 현재 가격이 스택의 top에 있는 가격보다 낮을 때
        while stack and price < prices[stack[-1]]:
            j = stack.pop()  # 스택에서 가격이 떨어진 시점을 pop합니다.
            answer[j] = i - j  # 가격이 떨어지지 않은 기간을 계산합니다.
        # 현재 시점을 스택에 push합니다.
        stack.append(i)
    
    # 스택에 남아있는 시점들에 대해 가격이 떨어지지 않은 기간을 계산합니다.
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    
    return answer

def solution(prices):
    times = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        for s,idx in stack:
            times[idx] += 1
        while stack and stack[-1][0] > prices[i]:
            stack.pop()
        stack.append((prices[i], i))
    return times

# def solution5(prices):
#     times = [0] * len(prices)
#     stack = []
#     for i in range(len(prices)):
#         for s, idx in stack:
#             times[idx] += 1
#     for price in prices:
        
