def solution(clothes):
    cloth_dict = {}
    for cloth in clothes:
        name = cloth[0]
        kind = cloth[1]
        if kind in cloth_dict:
            cloth_dict[kind] += 1
        else:
            cloth_dict[kind] = 1
    print(list(cloth_dict.values()))
    # return answer