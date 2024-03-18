def solution(people, limit):
    answer = 0
    people.sort() # 정렬 후 몸무게 큰 사람과 작은사람 짝지어야 많이 태울 수 있을 듯 -> index 클수록 무거운 사람
    
    start = 0
    end = len(people) - 1
    
    while (start <= end):
        if (people[start]+people[end] <=limit): # limit 보다 작거나 같으면 둘다 구출 가능
            start += 1 # 가능할 경우 start도 구출
            end -= 1 # 가능할 경우 end도 구출
        else:
            end -= 1 # 안되면 무거운 사람부터 먼저 구출
        answer += 1
    return answer
#     q = deque()
#     people.sort()
#     while q and sum(q) <= limit:
#         person = people.pop(0)
#         q.append(person)
#         print(q)
#     answer = 0
#     return answer