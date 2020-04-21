import math
import random
import matplotlib.pyplot as plt
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
        if np.mod(exp, 2):
            c = np.mod(c*a, m)

        a = np.mod(a*a, m)
        exp = np.floor_divide(exp, 2)

    return c

def DFT(prob, n_states):
    new_prob = np.empty(n_states, dtype=np.double)
    for k in range(n_states):
        c = np.complex()
        for j in range(n_states):
            theta = -2*math.pi*k*j / n_states
            c += math.sqrt(prob[j]) * np.complex(math.cos(theta), math.sin(theta))

        new_prob[k] = (c * c.conjugate()).real / n_states

    return new_prob

def shor(n):
    if is_prime(n):
        raise Exception("n must be a composite number")

    if is_prime_power(n):
        raise Exception("n cannot be a power of a prime")

    found = False
    while not found:
        x = random.randint(2, n-1)
        gcd = math.gcd(x, n)

        print(x)
        if gcd != 1:
            found = True
            factors = [gcd, n // gcd]

        r = get_order(x, n)

        print("R")

        if r % 2 == 0 and x**(r/2) != n-1:
            found = True
            r = r // 2
            factors = [math.gcd(y, n) for y in [x**r - 1, x**r + 1]]

    return factors

def get_order(x, n):
    # Quantum
    t = math.floor(2 * math.log2(n)) + 1
    n_states = 2**t

    r = 1
    while x != 1 and r < n:
        m = 0
        while m == 0:
            m = quantum(x, n, n_states)

        # first term of the continued fractions
        coef = []
        f = Fraction(m, n_states)
        while f != 0:
            f = 1 / f
            i = int(f)
            f = f - i
            coef.append(i)

        convergents = [Fraction(1,1)]
        for last in range(len(coef)):
            c = Fraction(1,coef[last])
            for idx in reversed(range(last)):
                c += Fraction(coef[idx], 1)
                c = 1 / c
            convergents.append(c)

        f = 1
        for c in convergents:
            if c.denominator < n:
                f = c.denominator

        x = (x ** f) % n
        r *= f

        print(m, f)
        print( x, r)

    return r

def quantum(x, n, n_states):
    p = np.empty(n_states, dtype=np.double)

    # phi_0 and phi_2 are only used for demonstrating the usage
    p = phi_1(p, n_states)
    p = phi_3(p, n_states, x, n)
    p = phi_4(p, n_states)

    measure = np.random.choice(range(n_states), p=p)
    return measure

def phi_0(p, n_states):
    p.fill(0)
    p[0] = 1
    return p

def phi_1(p, n_states):
    p.fill(1 / n_states)
    return p

def phi_2(x, n, p, n_states):
    freq_powers = np.zeros(n, dtype=np.double)

    power = 1
    for j in range(n_states):
        freq_powers[power] += prob[j]
        power = (power * x) % n

    return freq_powers

def phi_3(p, n_states, x, n):
    random_j = random.randint(0, n_states-1)
    x_b = power_mod(x, random_j, n)

    cnt = 0
    power = 1
    for j in range(n_states):
        if x_b == power:
            cnt += 1
        power = (power * x) % n

    power = 1
    for j in range(n_states):
        if x_b == power:
            p[j] = 1 / cnt
        else:
            p[j] = 0
        power = (power * x) % n
    return p

def phi_4(p, n_states):
    return DFT(p, n_states)
