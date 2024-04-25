def solution(my_string, m, c):
    answer = ''
    
    c -= 1
    while c < len(my_string):
        answer += my_string[c]
        c += m
    
    return answer
    #return my_string[c-1::m]