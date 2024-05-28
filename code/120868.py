#120868
def solution(sides):
    answer = 0
    s, e = sorted(sides)
    for i in range(e+1):
        if s+i > e:
            answer += 1

    for i in range(e+1, s+e+1):
        if s+e > i:
            answer += 1
            
    return answer