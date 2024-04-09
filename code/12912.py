def solution(a, b):
    answer = [int(a), int(b)]
    answer.sort()
    result = 0
    for i in range(answer[0], answer[1]+1):
        result += i
    return result

print(solution(3, 5))