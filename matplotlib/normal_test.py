
import numpy as np
import matplotlib.pyplot as plt

ss = np.random.normal(0, 1, 10000000)

plt.hist(ss, bins=1000, normed=True)

plt.show()
