def solution(a, d, included):
    answer = 0
    ap = []
    count = 0
    while count < len(included):
        ap.append(a+d*count)
        count += 1
    
    for i in range(len(included)):
        if included[i]:
            answer += ap[i]
            #answer += a+i*d
        
    return answer