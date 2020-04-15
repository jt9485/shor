import math
import random
import numpy as np

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
    #TODO filter powers of odd primes

    while n % 2 == 0:
        n /= 2

    found = False
    while not found:
        x = random.randint(2, n-1)
        gcd = math.gcd(x, n)

        if gcd != 1:
            found = True
            factors = [gcd, n / gcd]

        r = shor_quantum(n, x)

        #TODO extract the denominator

        if r % 2 == 0 and x**(r/2) % n != n-1:
            found = True
            factors = [math.gdc(y, n) for y in [x**(r/2) - 1, x**(r/2) + 1]]

    return factors

#TODO
def shor_quantum(N, x):
    order = 1
    n = math.ceil(math.log2(N))
    t = math.ceil(math.log2(N**2))

    # phi_0 = |0...0>
    reg_sz = t+n
    reg_num_states = 1

    # phi_1 = \frac{1}{\sqrt{2^t}} \sum_{j=0}^{2^t-1}|j>|0>
    reg_num_states = 2**t

    # phi_2 = \frac{1}{\sqrt{2^t}} \sum_{j=0}^{2^t-1}|j>|x^j \Mod{N}>

    # phi_3 after measuring second register

    # Measure
    j = random.randint(0, 2**t-1)
    x_b = power_mod(x, j, N)
    prob = np.empty(2**t, dtype=np.double)

    # probability not equal anymore
    reg_num_states = 0
    for j in range(2**t):
        if x_b == power_mod(x, j, N):
            reg_num_states += 1

    for j in range(2**t):
        if x_b == power_mod(x, j, N):
            prob[j] = 1 / reg_num_states
        else:
            prob[j] = 0

    # phi_4 apply reverse DFT
    prob = DTF(prob, 2**t)

    # phi_5 after measuring all qubits

    measure = np.random.choice(range(2**t), p=prob)

    # continued fractions
    a0 = math.floor(2**t / measure)
    
    r = r * a0
    
    if power_mod(x, r, N) != 1:
        x = x**r
    else:
        found = True

    return order
