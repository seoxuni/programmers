#120878
import math
def solution(a, b):
    n = b / math.gcd(a, b)
    
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 1

    factors = list(set(factors))

    if 2 in factors:
        factors.remove(2)
    if 5 in factors:
        factors.remove(5)
    
    return 1 if len(factors) == 0 else 2