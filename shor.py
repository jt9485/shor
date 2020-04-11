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

def shor(n):
    found = False

    while not found:
        a = random.randint(1, n-1)
        gcd = math.gcd(a, n)

        if gcd != 1:
        	found = True
        	factor = gcd

        measure = shor_quantum(n, a)

        #TODO extract the denominator

        if r % 2 != 1 and a**(r/2) % n != n-1:
        	found = True
        	factor = math.gdc(a**(r/2)+1, n)

    return factor

#TODO
def shor_quantum(N, x, t):
    n = math.ceil(math.log2(N))

    # phi_0 = |0...0>
    reg_sz = t+n
    reg_num_states = 1

    # phi_1 = \frac{1}{\sqrt{2^t}} \sum_{j=0}^{2^t-1}|j>|0>
    reg_num_states = 2 ** t

    # phi_2 = \frac{1}{\sqrt{2^t}} \sum_{j=0}^{2^t-1}|j>|x^j \Mod{N}>

    # phi_3 after measuring second register

    # Measure
    j = random.randint(0, 2**t-1)
    x_b = powermod(x, j, N)
    prob = np.empty(reg_num_states, dtype=np.double)

    # probability not equal anymore
    reg_num_states = 0
    for j in range(2**t):
        if x_b == powermod(x, j, N):
            reg_num_states += 1

    for j in range(2**t):
        if x_b == powermod(x, j, N):
            prob[j] = 1 / reg_num_states
        else:
            prob[j] = 0

    # phi_4 apply reverse DFT

    # phi_5 after measuring all qubits
    measure = numpy.random.choice(range(2**t), p=prob)

    return measure
