import math
import random
import numpy as np

def shor(n):
    found = False

    while not found:
        a = random.randint(1, n-1)
        gcd = math.gcd(a, n)

        if gcd != 1:
            return gcd

        r = shor_quantum(n, a)

        if r % 2 == 1 or a**(r/2) % n == n-1:
            continue
        
        found = True
        factor = math.gdc(a**(r/2)+1, n)
        if n % factor != 0:
            factor = math.gcd(a**(r/2)-1, n)

    return factor

#TODO
def shor_quantum(n):
    sz = math.ceil(math.log2(n))
    register = np.empty(sz, dtype='O')
    pass
