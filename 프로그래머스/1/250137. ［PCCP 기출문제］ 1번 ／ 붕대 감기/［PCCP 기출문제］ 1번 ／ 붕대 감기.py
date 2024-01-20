def solution(bandage, health, attacks):
    t, x, y = bandage
    i = 0
    success = 0
    hp = health
    attack_dict = {}
    for attack in attacks:
        attack_dict[attack[0]] = attack[1] 
    for i in range(1, attacks[-1][0]+1):
        print(i, hp, success)
        if i in attack_dict.keys(): #attack.keys -> 공격 시간
            success = 0 # success를 0으로  
            hp -= attack_dict[i] # i에 해당하는 피해량만큼 체력 감소
            if hp <= 0: # 현재 체력이 0 이하라면
                return -1
        else:
            success += 1 # 연속 성공 + 1
            hp += x # 현재 체력 + 초당 회복량
            if hp >= health: # 결과가 최대 체력 이상이라면
                hp = health # 현재 체력 = 최대 체력
        if success == t:
            hp += y # 추가 체력 부여 받는다
            success = 0 # 연속 성공을 0으로 초기화
        print(i, hp, success)
    return hp