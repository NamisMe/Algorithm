# from collections import deque
def solution1(s):
    parsed_s = s.replace(')(', '),(').split(',')
    print(parsed_s)
    for ps in parsed_s:
        q = deque(ps)
        # print(q)
        while q:
            left = q.popleft()
            right = q.pop()
            print(left, right)
            if (left == '(' and right == ')'):
                continue
            else:
                return False
                break
        return True
    
def solution(s):
    # 스택 초기화
    stack = []

    # 주어진 문자열 s를 순회
    for char in s:
        # 만약 현재 문자가 '('라면 스택에 추가
        if char == '(':
            stack.append(char)
        else: # 현재 문자가 ')'라면
            # 스택이 비어있으면 짝이 맞지 않는 경우이므로 False 반환
            if not stack:
                return False
            # 스택에서 마지막 '('를 제거
            stack.pop()

    # 모든 검사를 마친 후 스택이 비어있으면 괄호의 짝이 모두 맞는 것이므로 True 반환, 그렇지 않으면 False 반환
    return not stack

