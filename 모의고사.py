def solution(answers):
    #score 초기화
    score_list = [0,0,0]
    
    # 각 방식 구현
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    #정답과 비교
    for i, a in enumerate(answers):
        if a == first[i % len(first)]:
            score_list[0] += 1
        if a == second[i % len(second)]:
            score_list[1] += 1
        if a == third[i % len(third)]:
            score_list[2] += 1
            
    
    # 최댓값의 index 찾는 과정 
    answer = [i + 1 for i, score in enumerate(score_list) if score == max(score_list)]
    return answer