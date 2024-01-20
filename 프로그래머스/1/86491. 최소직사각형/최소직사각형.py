def solution(sizes):
    w_list = []
    h_list = []
    for size in sizes:
        size.sort()
        w_list.append(size[0])
        h_list.append(size[1])
    return max(w_list) * max(h_list)
    # print(height, width)
    # return answer