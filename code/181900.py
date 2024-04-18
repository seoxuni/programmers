def solution(my_string, indices):
    strArr = list(my_string)
    
    for idx in indices:
        strArr[idx] = ''
        
    return ''.join(strArr)