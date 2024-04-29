#등수 매기기
def solution(score):
    answer = []
    s1 = []
    
    for (a, b) in score:
        s1.append(a+b)
    
    s2 = sorted(s1, reverse=True)
    for i in s1:
        answer.append(s2.index(i)+1)
    
    return answer