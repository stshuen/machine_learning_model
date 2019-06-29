# -*- coding: utf-8 -*-
# Example: Calculate ∫sin(x)xdx

import matplotlib.pyplot as plt
import numpy as np
# The function has a shape that is similar to Gaussian and therefore
# we choose here a Gaussian as importance sampling distribution.
from scipy.stats import norm

mu = 2
sig = .7
f = lambda x: np.sin(x) * x
infun = lambda x: np.sin(x) - x * np.cos(x)
p = lambda x: (1 / np.sqrt(2 * np.pi * sig ** 2)) * np.exp(-(x - mu) ** 2 / (2.0 * sig ** 2))
normfun = lambda x: norm.cdf(x - mu, scale=sig)

plt.figure(figsize=(18, 8))  # set the figure size
# range of integration
xmax = np.pi
xmin = 0
# Number of draws
N = 1000
# Just want to plot the function
x = np.linspace(xmin, xmax, 1000)
plt.subplot(1, 2, 1)
plt.plot(x, f(x), 'b', label=u'Original $x\sin(x)$')
plt.plot(x, p(x), 'r', label=u'Importance Sampling Function: Normal')
plt.xlabel('x')
plt.legend()
# =============================================
# EXACT SOLUTION
# =============================================
Iexact = infun(xmax) - infun(xmin)
print
Iexact
# ============================================
# VANILLA MONTE CARLO
# ============================================
Ivmc = np.zeros(1000)
for k in np.arange(0, 1000):
    x = np.random.uniform(low=xmin, high=xmax, size=N)
    Ivmc[k] = (xmax - xmin) * np.mean(f(x))
# ============================================
# IMPORTANCE SAMPLING
# ============================================
# CHOOSE Gaussian so it similar to the original functions

# Importance sampling: choose the random points so that
# more points are chosen around the peak, less where the integrand is small.
Iis = np.zeros(1000)
for k in np.arange(0, 1000):
    # DRAW FROM THE GAUSSIAN: xis~N(mu,sig^2)
    xis = mu + sig * np.random.randn(N, 1)
    xis = xis[(xis < xmax) & (xis > xmin)]
    # normalization for gaussian from 0..pi
    normal = normfun(np.pi) - normfun(0)  # 注意:概率密度函数在采样区间[0 pi]上的积分需要等于1
    Iis[k] = np.mean(f(xis) / p(xis)) * normal  # 因此,此处需要乘一个系数即p(x)在[0 pi]上的积分
plt.subplot(1, 2, 2)
plt.hist(Iis, 30, histtype='step', label=u'Importance Sampling')
plt.hist(Ivmc, 30, color='r', histtype='step', label=u'Vanilla MC')
plt.vlines(np.pi, 0, 100, color='g', linestyle='dashed')
plt.legend()
plt.show()
