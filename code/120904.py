def solution(num, k):
    answer = 0
    numArr = list(map(int, str(num)))
    
    if k in numArr:
        answer = numArr.index(k) + 1
    else:
        answer = -1
        
    return answer