def solution1(citations):
    answer = 0 
    citations.sort(reverse=True) # citations 정렬
    print(citations)
    for h in range(citations[0], 0, -1): #높은 숫자부터 거꾸로 정렬
        over_count, under_count = 0, 0 # h번 이상 인용된 논문 수, h번 이하 인용된 논문 수 초기화
        for citation in citations: 
            if citation >= h: 
                over_count += 1
            elif citation <= h:
                under_count += 1
        # 최대 h를 구하는 것이므로 큰 것부터 줄여나가자라는 생각
        if (over_count >= h) and (under_count <= h): # 줄여나가다가 이 조건을 만족한 순간.
            answer = h
            break
    return answer

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # #1
    # for i, citation in enumerate(citations):
    #     print(i, citation)
    #     if citation >= i+1 :      
    #         answer = i+1
    #2
    for citation in citations:
        if citation >= citations.index(citation)+1:
            answer = citations.index(citation)+1
    return answer