#12982
def solution(d, budget):
    answer = 0
    t = 0
    for i in sorted(d):
        t += i
        if t <= budget:
            answer += 1
    return answer