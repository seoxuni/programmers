def solution(arr):
    arrIdx = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            arrIdx.append(i)
    
    return arr[arrIdx[0]:arrIdx[-1]+1] if arrIdx else [-1]