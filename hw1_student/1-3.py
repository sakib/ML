#!/usr/bin/python
from scipy.special import gamma
from math import sqrt, e, pi
import matplotlib.pyplot as plt

# unit hypersphere surface area
S = lambda d: pow(pi, (d+1)/2) / gamma((d+1)/2.)
sigma = 1.
D = [1., 2., 5., 10., 20.]

def p_r(d):
    print(d)
    r = sqrt(d)*sigma #r*
    num = S(d)*pow(r, d-1)
    denom = pow(2.*pi*sigma**2., d/2.)
    expo = -(r**2.)/(2.*sigma**2.)
    print num, denom, expo
    print(num/denom * e**expo)
    return num/denom * e**expo

plt.plot(D, map(p_r, D), 'ro')
plt.axis([0, 22, 0, 1])
plt.xlabel('d')
plt.ylabel('p(r|d)')
plt.show()
