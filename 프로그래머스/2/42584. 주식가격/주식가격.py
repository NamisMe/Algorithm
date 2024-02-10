def solution(prices):
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