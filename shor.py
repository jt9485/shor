import math
import random

import classical
from quantum import quantum

# ________
# | shor |
# --------
# Given a natural n that is neither even nor prime nor a power of a single 
# prime it find two divisors for it. If n is even a divisor has already been
# found

def shor(n):
    if n % 2 == 0:
        raise Exception("n must not be even")

    if classical.is_prime(n):
        raise Exception("{} must be a composite number".format(n))

    if classical.is_prime_power(n):
        raise Exception("{} cannot be a power of a prime".format(n))

    while True:
        x = random.randint(2, n-1)
        gcd = math.gcd(x, n)

        if gcd != 1:
            print("Lucky find!!")
            return [gcd, n // gcd]

        r = get_order(x, n)

        if r != None and r % 2 == 0:
            y = classical.power_mod(x, r // 2, n)
            if y != n-1 and y != 1:
                return [math.gcd(y+1, n), math.gcd(y-1, n)]

# _____________
# | get_order |
# -------------
# Given x, n coprime natural numbers computes ord(x) mod n using quantum
# ---------------------------------------------------------------
# Note: it is not guaranteed that this function will find the actual order of x

def get_order(x, n):
    t = math.floor(2 * math.log2(n)) + 1 # so that N^2 <= 2^t < 2*N^2

    print("-------------------->\nget_order: x={}, n={}".format(x, n))

    r = 1
    while x != 1 and r < n:
        m = quantum(x, n, t)

        while m == 0:
            print("[F] : MEASURED : 0")
            m = quantum(x, n, t)

        print("[T] : MEASURED : {}".format(m))
        coeficients = classical.get_coeficients(m, 2**t)
        convergents = classical.get_convergents(coeficients)

        d = 1
        for c in convergents:
            if c.denominator < n:
                d = c.denominator

        x = classical.power_mod(x, d, n)
        r *= d

    print("Estimated r: {}".format(r))

    if x == 1 and r < n:
        return r

    return None
