import math
import random

import classical
import numpy as np

# ___________
# | quantum |
# -----------
# Given x and natural coprime numbers and t the number qubits on the first
# register performs the quantum part of the shor algorithm and returns the
# measured value theta

def quantum(x, n, t):
    n_states = 2 ** t
    p = np.empty(n_states, dtype=np.double)

    # psi_0 and psi_2 are only used for demonstrating the usage
    p = psi_1(p, n_states)
    p = psi_3(x, n, p, n_states)
    p = psi_4(p, n_states)

    measure = np.random.choice(range(n_states), p=p)
    return measure

# STAGE psi_0 : all quibits on both registers are initialized to 0
def psi_0(p, n_states):
    p.fill(0)
    p[0] = 1
    return p

# STAGE psi_1 : application of Hadamard operator, all possible 2^t states upon
# measurement on the first register are equaly probable
def psi_1(p, n_states):
    p.fill(1 / n_states)
    return p

# STAGE psi_2 : applies the linear operator V_x : |j|k> >--> |j|k+x^j \divmod n>
# to the register therefore calculating the 2**t first powers of x \divmod n
def psi_2(x, n, p, n_states):
    freq_powers = np.zeros(n, dtype=np.double)

    power = 1
    for j in range(n_states):
        freq_powers[power] += p[j]
        power = (power * x) % n

    return freq_powers

# STAGE psi_3 : measures the second register collapsing all the values of the first
# register to those whose power of x is equivalent mod n
def psi_3(x, n, p, n_states):
    random_j = random.randint(0, n_states-1)
    x_b = classical.power_mod(x, random_j, n)

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

# STAGE psi_4 : applies the quantum discrete fourier transform to this first
# register
def psi_4(p, n_states):
    return DFT(p, n_states)

def DFT(prob, n_states):
    new_prob = np.empty(n_states, dtype=np.double)

    for k in range(n_states):
        c = np.complex()
        for j in range(n_states):
            theta = -2*math.pi*k*j / n_states
            c += math.sqrt(prob[j]) * np.complex(math.cos(theta), math.sin(theta))

        new_prob[k] = (c * c.conjugate()).real / n_states

    return new_prob
