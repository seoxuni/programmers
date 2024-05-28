#181857
def solution(arr):
    if (len(arr)&(len(arr)-1)) == 0:
        return arr
    for i in range(11):
        if len(arr) < 2**i:
            for _ in range(2**i - len(arr)):
                arr.append(0)
        else:
            continue
        break
    return arr