#181912
def solution(intStrs, k, s, l):
    strArr = [int(intStr[s:s+l]) for intStr in intStrs]
    return [i for i in strArr if i > k]