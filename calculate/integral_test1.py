# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

"""
使用蒙特卡洛法计算区间[2 3]上的定积分：∫(x^2+4*x*sin(x))dx
from: https://www.jb51.net/article/130511.htm
"""


def f(x):
    return x ** 2 + 4 * x * np.sin(x)


def intf(x):
    return x ** 3 / 3.0 + 4.0 * np.sin(x) - 4.0 * x * np.cos(x)


a = 2
b = 3
# use N draws
N = 10000
X = np.random.uniform(low=a, high=b, size=N)  # N values uniformly drawn from a to b
Y = f(X)  # CALCULATE THE f(x)
# 蒙特卡洛法计算定积分：面积=宽度*平均高度
Imc = (b - a) * np.sum(Y) / N
exactval = intf(b) - intf(a)
print
"Monte Carlo estimation=", Imc, "Exact number=", intf(b) - intf(a)
# --How does the accuracy depends on the number of points(samples)? Lets try the same 1-D integral
# The Monte Carlo methods yield approximate answers whose accuracy depends on the number of draws.
Imc = np.zeros(1000)
Na = np.linspace(0, 1000, 1000)
exactval = intf(b) - intf(a)
for N in np.arange(0, 1000):
    X = np.random.uniform(low=a, high=b, size=N)  # N values uniformly drawn from a to b
    Y = f(X)  # CALCULATE THE f(x)
    Imc[N] = (b - a) * np.sum(Y) / N

plt.plot(Na[10:], np.sqrt((Imc[10:] - exactval) ** 2), alpha=0.7)
plt.plot(Na[10:], 1 / np.sqrt(Na[10:]), 'r')
plt.xlabel("N")
plt.ylabel("sqrt((Imc-ExactValue)$^2$)")
plt.show()
