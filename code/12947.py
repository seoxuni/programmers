def solution(x):
    answer = list(map(int, str(x)))
    if x % int(sum(answer)) == 0:
        return True
    else:
        return False

print(solution(12))