import math
import random
import numpy as np

def shor(n):
    while True:
        a = random.randint(1, n-1)
        gcd = math.gcd(a, n)

        if gcd != 1:
            return gcd

        r = shor_quantum(n, a)

        if r % 2 == 1 or a**(r/2) % n == n-1:
            continue
        
        factor = math.gdc(a**(r/2)+1, n)
        if n % factor == 0:
            return factor
        else:
            return math.gcd(a**(r/2)-1, n)

#TODO
def shor_quantum(n):
    pass
