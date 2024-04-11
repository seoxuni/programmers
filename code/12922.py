def solution(n):
    answer = ''
    for i in range(n):
        if n > 0:
            answer += '수'
        if n > 1:
            answer += '박'
        n -= 2
    return answer

#   answer = "수박"*n
#   return answer[:n]