import math
def solution(n, m):
    lcm = 0
    for i in range(n, n*m+1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
    return [math.gcd(n, m), lcm]