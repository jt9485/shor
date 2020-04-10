import math
import random
import numpy as np

def shor(n):
    found = False

    while not found:
        a = random.randint(1, n-1)
        gcd = math.gcd(a, n)

        if gcd != 1:
        	found = True
        	factor = gcd

        r = shor_quantum(n, a)

        if r % 2 != 1 and a**(r/2) % n != n-1:
        	found = True
        	factor = math.gdc(a**(r/2)+1, n)

    return factor

#TODO
def shor_quantum(n):
    sz1 = random.randint(math.ceil(math.log2(n**2)), math.floor(2 * math.log2(n**2)))
    sz2 = math.ceil(math.log2(n))
    sz = sz1 + sz2
    register = np.empty(sz, dtype='O')
    pass
