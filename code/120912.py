#120912
def solution(array):
    answer = []
    for i in array:
        answer.extend(list(map(int, str(i))))
    return answer.count(7)