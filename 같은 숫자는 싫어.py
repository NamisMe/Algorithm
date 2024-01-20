def solution(arr):
    answer = []
    for a in arr:
        print(answer, answer[-1:])
        if answer[-1:] == [a] : continue
        answer.append(a)
    return answer