#120880
def solution(numlist, n):
    numlist = [[abs(i - n), i] for i in numlist]
    numlist.sort(key=lambda x: (x[0], -x[1]))    
    
    return [y for (x, y) in numlist]