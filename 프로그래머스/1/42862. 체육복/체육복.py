def solution(n, lost, reserve):
    #students 배열 만들기
    students = [1 for i in range(n)]
    answer = 0
    for r in reserve:
        students[r-1] += 1
    for l in lost:
        students[l-1] -= 1
    
    #greedy 알고리즘 적용해서 옷 빌려주기
    for i in range(n):
        #체육복이 없는 학생인 경우
        if students[i] == 0:
            # 앞 번호 학생이 여벌 체육복을 갖고 있는 경우
            if i > 0 and students[i-1] == 2:
                students[i] = 1
                students[i-1] = 1
            # 뒷 번호 학생이 여벌 체육복을 갖고 있는 경우
            elif i < n-1 and students[i+1] == 2:
                students[i] = 1
                students[i+1] = 1
                
    for i in range(n):
        if students[i] >= 1:
            answer += 1
    
    return answer