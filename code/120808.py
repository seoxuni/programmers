#분수의 덧셈
def solution(numer1, denom1, numer2, denom2):
    answer = []
    boonmo = denom1 * denom2
    boonja = numer1 * denom2 + numer2 * denom1
    
    start = max(boonmo, boonja)
    gcd = 1
    
    for num in range(start, 0, -1):
        if boonmo % num == 0 and boonja % num == 0:
            gcd = num
            break
    
    answer = [boonja / gcd, boonmo / gcd]
    return answer