def solution(my_strings, parts):
    answer = ''
    
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]    
    
    #for i in range(len(my_strings)):
    #    answer.append(my_strings[i][parts[i][0]:parts[i][1]+1])
    
    return answer