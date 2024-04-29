#수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    
    for (s, e, k) in queries:
        tmp = []
        for i in arr[s:e+1]:
            if i > k:
                tmp.append(i)
        
        try:
            answer.append(min(tmp))
        except:
            answer.append(-1)
            
    return answer