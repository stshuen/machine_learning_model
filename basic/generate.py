import matplotlib.pyplot as plt
import numpy as np

a1 = [i for i in range(100)]
print(a1)

a2 = (i for i in range(20))

print(a2.__next__())
print(next(a2))
for i in a2:
    print(i)


def test_generate(maxInt):
    """
    生成器
    :param maxInt:
    :return:
    """
    b, j, n = 1, 0, 0
    while n < maxInt:
        yield j
        b, j = b ** 0.1 + b, b
        n = n + 1
    return 'done'


plt.plot(np.linspace(1, 1000, 1000), [i for i in test_generate(1000)])
plt.show()
