from itertools import permutations

def solution(k, dungeons):
    answer = 0
    count_list = []
    for dungeons in permutations(dungeons): # dungeon의 조합
        fatigue = k # 현재 피로도를 k로 초기화
        count = 0
        for dungeon in dungeons:
            if fatigue >= dungeon[0]: # 최소 필요 피로도보다 k가 클 때
                fatigue -= dungeon[1]
                count += 1
            else:
                break
        count_list.append(count)
    answer = max(count_list)
    return answer