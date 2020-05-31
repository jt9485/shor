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
    if n < 2:
        return False

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
# Given three natural numbers a, exp and m returns a^b mod m

def power_mod(a, exp, m):
    c = 1
    while exp > 0:
        if exp % 2 != 0:
            c = (c*a) % m
        a = (a*a) % m
        exp = exp // 2

    return c

# ___________________
# | get_coeficients |
# -------------------
# 
# Given two natural numbers a and b returns the continued fraction as a list of
# integers

def get_coeficients(a, b):
    if b == 0:
        raise Exception("0 division is forbidden")

    coef = []
    while b != 0:
        coef.append(a // b)
        a, b = b, a % b

    return coef

# ___________________
# | get_convergents |
# -------------------
# Given a continued fraction as a non empty list of integers will return a list
# of convergents, per the continued fractions method

def get_convergents(coef):
    convergents = []

    p0, q0 = coef[0], 1
    convergents.append(Fraction(p0, q0))

    if len(coef) == 1:
        return convergents

    p1, q1 = coef[0]*coef[1] + 1, coef[1]
    convergents.append(Fraction(p1, q1))

    for c in coef[2:]:
        p0, p1 = p1, c*p1 + p0
        q0, q1 = q1, c*q1 + q0
        convergents.append(Fraction(p1, q1))

    return convergents
