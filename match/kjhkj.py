"""Exercise 11.1: Plotting a function
Plot the function
f(x) = sin2(x − 2)e−x2
over the interval [0; 2]. Add proper axis labels, a title, etc."""

import math

import matplotlib.pyplot as plt
import numpy as np


def fun(x):
    return math.sin(x - 2) ** 2 * math.exp(-x ** 2)


x = np.linspace(0, 2, num=1000)
plt.style.use('seaborn')
fun = np.vectorize(fun)
plt.plot(x, fun(x))
plt.xlabel('x')
plt.ylabel('y')
plt.title(
    r'$f(x)=sin^2(x)*(x-2)*e^{-x^2}$                                                                                                                                                ')
plt.show()
