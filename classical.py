import math
from fractions import Fraction

import numpy as np

def is_prime(n):
    d = 2
    while d*d < n:
        if n%d == 0:
            return False
        d += 1
    return True

def is_prime_power(n):
    m = math.ceil(math.log(n) / math.log(2))
    for i in range(1, m):
        root = math.pow(n, 1.0 / (i+1))
        if root == math.floor(root):
            return True
    return False

def power_mod(a, exp, m):
    c = 1
    while exp > 0:
        if exp % 2:
            c = (c*a) % m
        a = (a*a) % m
        exp = exp // 2

    return c

def get_denominators(f):
    coef = []
    while f != 0:
        f = 1 / f
        coef.append(int(f))
        f -= int(f)

    convergents = [Fraction(1,1)]
    for last in range(len(coef)):
        c = Fraction(1, coef[last])
        for idx in reversed(range(last)):
            c += Fraction(coef[idx], 1)
            c = 1 / c
        convergents.append(c)

    return [c.denominator for c in convergents]
