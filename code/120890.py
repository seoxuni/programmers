#120890
def solution(array, n):
    array.sort()
    testList = [abs(n - i) for i in array]
    
    return array[testList.index(min(testList))]