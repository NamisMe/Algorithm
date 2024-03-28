from collections import deque

def can_transform(word1, word2):
    # 두 단어 간에 변환 가능한지 확인하는 함수
    diff_count = sum(1 for x, y in zip(word1, word2) if x != y)
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set([begin])
    
    while q:
        current_word, steps = q.popleft()
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                q.append((word, steps + 1))
    
    return 0  # 변환할 수 없는 경우