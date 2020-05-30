import math
from fractions import Fraction

# ____________
# | is_prime |
# ------------
# Given a natural number n returns True if prime and False otherwise
# -------------------------------------------------------------------
# Note: this implementation is pseudopolynomial although a polynomial algorithm
# exists for this problem

def is_prime(n):
    if n < 2: 
        return False
    
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

# __________________
# | is_prime_power |
# ------------------
# Given a natural number n returns True if is of the type p^a with p prime and
# a natural greater than 1 and False otherwise
# -------------------------------------------------------------------
# Note: this implementation is pseudopolynomial because is_prime is as well
# If is_prime were polynomial this implemention would also be

def is_prime_power(n):
    if n == 0:
        return False

    if n == 1:
        return True

    m = math.ceil(math.log(n) / math.log(2))

    for i in range(1, m):
        root = math.pow(n, 1.0 / (i+1))
        if root == math.floor(root):
            if is_prime(math.floor(root)):
                return True
    return False

# _____________
# | power_mod |
# -------------
# Given three natural numbers a, exp and m returns a^b \divmod m

def power_mod(a, exp, m):
    c = 1
    while exp > 0:
        if exp % 2 != 0:
            c = (c*a) % m
        a = (a*a) % m
        exp = exp // 2

    return c

# ___________________
# | get_convergents |
# -------------------
# Given two natural numbers a and b will return a list of convergents, per the
# continued fractions method, to \frac{a}{b}
# -----------------------------------------------------------------------------
# Note: both numbers are supposed to be positive with a < b

def get_convergents(a, b):
    if a == 0:
        raise Exception("a must not be 0")

    if b == 0:
        raise Exception("0 division is forbidden")

    coef = []
    f = Fraction(a, b)
    while f != 0:
        f = 1 / f
        coef.append(int(f))
        f -= int(f)

    convergents = [Fraction(1,1)]
    for idx, x in enumerate(coef):
        c = Fraction(1, x)
        for y in reversed(coef[:idx]):
            c += Fraction(y, 1)
            c = 1 / c
        convergents.append(c)

    return convergents
