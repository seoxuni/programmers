#120884
def solution(chicken):
    answer = 0
    while True:
        if chicken >= 10:
            chicken -= 10
            answer += 1
            chicken += 1
        else:
            break
    return answer