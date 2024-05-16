#120861
def solution(n):
    answer = ''
    while n:
        answer += str(n % 3)
        n //= 3
        
    return int(answer, 3)   # int 함수로 3진법 표현