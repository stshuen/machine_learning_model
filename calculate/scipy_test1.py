# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from scipy.optimize import leastsq

"""
假设有一组实验数据(x[i], y[i])，我们知道它们之间的函数关系:y = f(x)，通过这些已知信息，需要确定函数中的一些参数项。
例如，如果f是一个线型函数f(x) = k*x+b，那么参数k和b就是我们需要确定的值。
如果将这些参数用 p 表示的话，那么我们就是要找到一组 p 值使得如下公式中的S函数最小：
S(\mathbf{p}) = \sum_{i=1}^m [y_i - f(x_i, \mathbf{p}) ]^2
最小二乘拟合
from: https://docs.huihoo.com/scipy/scipy-zh-cn/scipy_intro.html
"""


def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A * np.sin(2 * np.pi * k * x + theta)


def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)


x = np.linspace(0, -2 * np.pi, 100)
A, k, theta = 10, 0.34, np.pi / 6  # 真实数据的函数参数
y0 = func(x, [A, k, theta])  # 真实数据
y1 = y0 + 2 * np.random.randn(len(x))  # 加入噪声之后的实验数据

p0 = [7, 0.2, 0]  # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y1, x))

print(u"真实参数:", [A, k, theta])
print(u"拟合参数", plsq[0])  # 实验数据拟合后的参数

pl.plot(x, y0, label=u"真实数据")
pl.plot(x, y1, label=u"带噪声的实验数据")
pl.plot(x, func(x, plsq[0]), label=u"拟合数据")
pl.legend()
pl.show()
