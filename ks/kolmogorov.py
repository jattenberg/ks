import numpy as np
from math import sqrt, exp

def ks_statistic(obs_one, obs_two):
    cdf_one = np.sort(obs_one)
    cdf_two = np.sort(obs_two)

    i = 0
    j = 0
    d = 0.0
    fn1 = 0.0
    fn2 = 0.0
    l1 = float(len(cdf_one))
    l2 = float(len(cdf_two))

    while (i < len(cdf_one) and j < len(cdf_two)):
        d1 = cdf_one[i]
        d2 = cdf_two[j]
        if d1 <= d2:
            i = i + 1
            fn1 = i/l1
        if d2 <= d1:
            j = j + 1
            fn2 = j/l2
        dist = abs(fn2 - fn1)
        if dist > d:
            d = dist

    return d

def ks_significance(alam):
    EPS1 = 0.001
    EPS2 = 1.0e-8

    fac = 2.0
    sum = 0.0
    term_bf = 0.0

    a2 = -2.0*alam*alam
    for j in range(1, 100):
        term = fac*exp(a2*j*j)
        sum = sum + term
        if abs(term) <= EPS1 * term_bf or abs(term) <= EPS2 * sum:
            return sum
        fac = -fac
        term_bf = abs(term)

    return 1.0 # failing to converge
    
"""
  from numerical recipies
"""
def ks_test(obs_one, obs_two):
    d = ks_statistic(obs_one, obs_two)
    l1 = len(obs_one)
    l2 = len(obs_two)

    en = sqrt(float(l1*l2)/(l1 + l2))
    return ks_significance(en + 0.12 + 0.11/en) # magic numbers

