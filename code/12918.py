def solution(s):
    answer = True
    try:
        if type(int(s)) == int:
            answer = True
    except:
        answer = False
    
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        answer = False
        
    return answer

#   return s.isdigit() and len(s) in [4,6]