#86491
def solution(sizes):
    width = []
    height = []
    for (w, h) in sizes:
        if w > h:
            width.append(w)
            height.append(h)
        elif w < h:
            width.append(h)
            height.append(w)
        else:
            width.append(w)
            height.append(h)
    
    width.sort(reverse=True)
    height.sort(reverse=True)
    
    return width[0] * height[0]