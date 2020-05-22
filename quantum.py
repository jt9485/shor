import math
import random

import classical
import numpy as np

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

def phi_4(p, n_states):
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
