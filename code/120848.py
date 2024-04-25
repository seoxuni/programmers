def solution(n):
    answer = 0
    
    fac = 1
    for i in range(1, 11):
        fac *= i
        if fac > n:
            break
        answer = i
        
    return answer