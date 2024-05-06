#181860
def solution(arr, flag):
    x = []
    
    for i in range(len(arr)):
        if flag[i]:
            for _ in range(arr[i]*2):
                x.append(arr[i])
        else:
            for rm in range(arr[i]):
                del x[-1]
    
    return x
