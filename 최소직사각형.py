def solution(sizes):
    w_list = [size[0] for size in sizes]
    h_list = [size[1] for size in sizes]
    w, h = min(w_list), min(h_list)
    for size in sizes:
        print(w, h)
        if size[0] >= w or size[1] >= h:
            w, h = size[0], size[1]
        else:
            if size[1] >= w or size[0] >=h:
                w, h = size[1], size[0]
    return w * h