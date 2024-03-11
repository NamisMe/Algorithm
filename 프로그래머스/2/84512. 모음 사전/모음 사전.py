from itertools import permutations, combinations, product

def solution(word):
    words = []
    alpha_dict = ['A','E','I','O','U']
    
    for i in range(1, 6):
        for c in product(alpha_dict, repeat=i):
            words.append(''.join(list(c))) # 원소를 합치기
    words.sort()
    # print(words[:10])
    answer = words.index(word) + 1
    return answer